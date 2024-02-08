from cerberus import Validator

body = {
    "data": {
        "elemento1": 123,
        "elemento2": "olaMundo",
    }
}

body_validador = Validator({
    "data": {
        "type": "dict", 
        "schema": {
            "elemento1": { "type": "float", "required": True, "empty": False },
            "elemento2": { "type": "string", "required": True, "empty": True },
            "elemento3": { "type": "string", "required": False, "empty": False },
        }
    }
})

response = body_validador.validate(body)

if response is False:
    print(body_validador.errors)
else:
    print('Body OK')
