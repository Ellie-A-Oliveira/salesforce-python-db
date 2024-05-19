import re

def validate(dict, field_mapping):
    required_fields = [field_name for field_name, field in field_mapping.items() if field["validation_rules"] == ["required"]]
    for key, value in dict.items():
        if key not in field_mapping:
            raise Exception(f"Invalid field: {key}")
        validation_rules = field_mapping[key]["validation_rules"]
        for rule in validation_rules:
            if rule == "required" and value is None:
                raise Exception(f"Field {key} is required")
            if rule == "email" and not re.match(r"[^@]+@[^@]+\.[^@]+", value):
                raise Exception(f"Invalid email format for field {key}")

    for field_name in required_fields:
        if dict.get(field_name) is None:
            raise Exception(f"Field {field_name} is required")
        
    return True


def create_class(class_name, field_mapping, db_table_name):
    class_attributes = {attr_name: None for attr_name in field_mapping.keys()}
    
    @classmethod
    def create_from_dict(cls, dict):
        validate(dict, field_mapping)
        instance = cls.__new__(cls)
        for key, value in dict.items():
            if key in field_mapping:
                setattr(instance, key, value)
        return instance
    
    def init_method(self):
        raise Exception("Use create_from_dict to create an instance")
    
    def repr_method(self):
        return f"{self.__class__.__name__}(id={self.id}, {', '.join([f'{key}={value}' for key, value in self.__dict__.items() if key != 'id'])})"
    
    def to_dict(self):
        return {key: value for key, value in self.__dict__.items()}
    
    def map_to_db(self):
        mapped_dict = {}
        for key, value in field_mapping.items():
            if "is_pk" in value and value["is_pk"]:
                continue
            if "db_field_name" in value:
                mapped_dict[value["db_field_name"]] = getattr(self, key)
                
        return mapped_dict
    
    class_attributes["__init__"] = init_method
    class_attributes["__repr__"] = repr_method
    class_attributes["create_from_dict"] = create_from_dict
    class_attributes["validate"] = validate
    class_attributes["to_dict"] = to_dict
    class_attributes["map_to_db"] = map_to_db
    
    class_attributes["db_table_name"] = db_table_name
    class_attributes["field_mapping"] = field_mapping
    
    return type(class_name, (object,), class_attributes)
    
    