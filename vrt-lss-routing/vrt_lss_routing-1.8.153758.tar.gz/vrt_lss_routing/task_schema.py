{
    "properties": {
        "departure_time": {
            "format": "date-time",
            "type": "string",
            "x-description-en": "Translation in progress"
        },
        "detail": {
            "default": true,
            "type": "boolean",
            "x-description-en": "Translation in progress"
        },
        "geo_provider": {
            "type": "string",
            "x-description-en": "Translation in progress"
        },
        "result_timezone": {
            "default": 0,
            "format": "int32",
            "maximum": 11,
            "minimum": -11,
            "type": "integer",
            "x-description-en": "Translation in progress"
        },
        "transport_type": {
            "default": "CAR",
            "enum": [
                "CAR",
                "TRUCK",
                "CAR_GT",
                "TUK_TUK",
                "BICYCLE",
                "PEDESTRIAN",
                "PUBLIC_TRANSPORT"
            ],
            "type": "string",
            "x-description-en": "Translation in progress"
        },
        "waypoints": {
            "items": {
                "nullable": true,
                "properties": {
                    "duration": {
                        "default": 0,
                        "format": "int32",
                        "maximum": 1440,
                        "minimum": 0,
                        "type": "integer",
                        "x-description-en": "Translation in progress"
                    },
                    "latitude": {
                        "format": "float",
                        "maximum": 90,
                        "minimum": -90,
                        "type": "number",
                        "x-description-en": "Translation in progress"
                    },
                    "longitude": {
                        "format": "float",
                        "maximum": 180,
                        "minimum": -180,
                        "type": "number",
                        "x-description-en": "Translation in progress"
                    }
                },
                "required": [
                    "latitude",
                    "longitude"
                ],
                "type": "object",
                "x-description-en": "Translation in progress"
            },
            "maxItems": 7000,
            "minItems": 2,
            "type": "array",
            "uniqueItems": false,
            "x-description-en": "Translation in progress"
        }
    },
    "required": [
        "waypoints"
    ],
    "type": "object",
    "x-description-en": "Translation in progress"
}