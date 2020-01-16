{
    "properties": {
        "merchandiser_settings": {
            "properties": {
                "accuracy": {
                    "default": "DAY",
                    "enum": [
                        "EXACT",
                        "DAY",
                        "CUSTOM_1",
                        "CUSTOM_2",
                        "CUSTOM_3"
                    ],
                    "type": "string",
                    "x-description-en": "Translation in progress"
                }
            },
            "type": "object",
            "x-description-en": "Translation in progress"
        },
        "orders": {
            "items": {
                "properties": {
                    "duration": {
                        "format": "float",
                        "type": "number",
                        "x-description-en": "Translation in progress"
                    },
                    "facts": {
                        "items": {
                            "properties": {
                                "time_window": {
                                    "properties": {
                                        "from": {
                                            "format": "date-time",
                                            "type": "string",
                                            "x-description-en": "Translation in progress"
                                        },
                                        "to": {
                                            "format": "date-time",
                                            "type": "string",
                                            "x-description-en": "Translation in progress"
                                        }
                                    },
                                    "required": [
                                        "from",
                                        "to"
                                    ],
                                    "type": "object",
                                    "x-description-en": "Translation in progress"
                                }
                            },
                            "required": [
                                "time_window"
                            ],
                            "type": "object",
                            "x-description-en": "Translation in progress"
                        },
                        "maxItems": 100,
                        "minItems": 0,
                        "type": "array",
                        "uniqueItems": true,
                        "x-description-en": "Translation in progress"
                    },
                    "key": {
                        "type": "string",
                        "x-description-en": "Translation in progress"
                    },
                    "location": {
                        "nullable": true,
                        "properties": {
                            "arrival_duration": {
                                "default": 0,
                                "format": "int32",
                                "maximum": 1440,
                                "minimum": 0,
                                "type": "integer",
                                "x-description-en": "Translation in progress"
                            },
                            "departure_duration": {
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
                    "reward": {
                        "format": "float",
                        "type": "number",
                        "x-description-en": "Translation in progress"
                    },
                    "visits": {
                        "items": {
                            "properties": {
                                "time_window": {
                                    "properties": {
                                        "from": {
                                            "format": "date-time",
                                            "type": "string",
                                            "x-description-en": "Translation in progress"
                                        },
                                        "to": {
                                            "format": "date-time",
                                            "type": "string",
                                            "x-description-en": "Translation in progress"
                                        }
                                    },
                                    "required": [
                                        "from",
                                        "to"
                                    ],
                                    "type": "object",
                                    "x-description-en": "Translation in progress"
                                }
                            },
                            "required": [
                                "time_window"
                            ],
                            "type": "object",
                            "x-description-en": "Translation in progress"
                        },
                        "maxItems": 100,
                        "minItems": 1,
                        "type": "array",
                        "uniqueItems": true,
                        "x-description-en": "Translation in progress"
                    }
                },
                "required": [
                    "key",
                    "location",
                    "visits",
                    "duration",
                    "reward"
                ],
                "type": "object",
                "x-description-en": "Translation in progress"
            },
            "maxItems": 7000,
            "minItems": 1,
            "type": "array",
            "uniqueItems": true,
            "x-description-en": "Translation in progress"
        },
        "performer": {
            "properties": {
                "finish_location": {
                    "nullable": true,
                    "properties": {
                        "arrival_duration": {
                            "default": 0,
                            "format": "int32",
                            "maximum": 1440,
                            "minimum": 0,
                            "type": "integer",
                            "x-description-en": "Translation in progress"
                        },
                        "departure_duration": {
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
                "key": {
                    "type": "string",
                    "x-description-en": "Translation in progress"
                },
                "shifts": {
                    "items": {
                        "properties": {
                            "availability_time": {
                                "properties": {
                                    "from": {
                                        "format": "date-time",
                                        "type": "string",
                                        "x-description-en": "Translation in progress"
                                    },
                                    "to": {
                                        "format": "date-time",
                                        "type": "string",
                                        "x-description-en": "Translation in progress"
                                    }
                                },
                                "required": [
                                    "from",
                                    "to"
                                ],
                                "type": "object",
                                "x-description-en": "Translation in progress"
                            },
                            "trip": {
                                "properties": {
                                    "actions": {
                                        "items": {
                                            "properties": {
                                                "location_time": {
                                                    "properties": {
                                                        "from": {
                                                            "format": "date-time",
                                                            "type": "string",
                                                            "x-description-en": "Translation in progress"
                                                        },
                                                        "to": {
                                                            "format": "date-time",
                                                            "type": "string",
                                                            "x-description-en": "Translation in progress"
                                                        }
                                                    },
                                                    "required": [
                                                        "from",
                                                        "to"
                                                    ],
                                                    "type": "object",
                                                    "x-description-en": "Translation in progress"
                                                },
                                                "order": {
                                                    "properties": {
                                                        "duration": {
                                                            "format": "float",
                                                            "type": "number",
                                                            "x-description-en": "Translation in progress"
                                                        },
                                                        "facts": {
                                                            "items": {
                                                                "properties": {
                                                                    "time_window": {
                                                                        "properties": {
                                                                            "from": {
                                                                                "format": "date-time",
                                                                                "type": "string",
                                                                                "x-description-en": "Translation in progress"
                                                                            },
                                                                            "to": {
                                                                                "format": "date-time",
                                                                                "type": "string",
                                                                                "x-description-en": "Translation in progress"
                                                                            }
                                                                        },
                                                                        "required": [
                                                                            "from",
                                                                            "to"
                                                                        ],
                                                                        "type": "object",
                                                                        "x-description-en": "Translation in progress"
                                                                    }
                                                                },
                                                                "required": [
                                                                    "time_window"
                                                                ],
                                                                "type": "object",
                                                                "x-description-en": "Translation in progress"
                                                            },
                                                            "maxItems": 100,
                                                            "minItems": 0,
                                                            "type": "array",
                                                            "uniqueItems": true,
                                                            "x-description-en": "Translation in progress"
                                                        },
                                                        "key": {
                                                            "type": "string",
                                                            "x-description-en": "Translation in progress"
                                                        },
                                                        "location": {
                                                            "nullable": true,
                                                            "properties": {
                                                                "arrival_duration": {
                                                                    "default": 0,
                                                                    "format": "int32",
                                                                    "maximum": 1440,
                                                                    "minimum": 0,
                                                                    "type": "integer",
                                                                    "x-description-en": "Translation in progress"
                                                                },
                                                                "departure_duration": {
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
                                                        "reward": {
                                                            "format": "float",
                                                            "type": "number",
                                                            "x-description-en": "Translation in progress"
                                                        },
                                                        "visits": {
                                                            "items": {
                                                                "properties": {
                                                                    "time_window": {
                                                                        "properties": {
                                                                            "from": {
                                                                                "format": "date-time",
                                                                                "type": "string",
                                                                                "x-description-en": "Translation in progress"
                                                                            },
                                                                            "to": {
                                                                                "format": "date-time",
                                                                                "type": "string",
                                                                                "x-description-en": "Translation in progress"
                                                                            }
                                                                        },
                                                                        "required": [
                                                                            "from",
                                                                            "to"
                                                                        ],
                                                                        "type": "object",
                                                                        "x-description-en": "Translation in progress"
                                                                    }
                                                                },
                                                                "required": [
                                                                    "time_window"
                                                                ],
                                                                "type": "object",
                                                                "x-description-en": "Translation in progress"
                                                            },
                                                            "maxItems": 100,
                                                            "minItems": 1,
                                                            "type": "array",
                                                            "uniqueItems": true,
                                                            "x-description-en": "Translation in progress"
                                                        }
                                                    },
                                                    "required": [
                                                        "key",
                                                        "location",
                                                        "visits",
                                                        "duration",
                                                        "reward"
                                                    ],
                                                    "type": "object",
                                                    "x-description-en": "Translation in progress"
                                                },
                                                "order_time": {
                                                    "properties": {
                                                        "from": {
                                                            "format": "date-time",
                                                            "type": "string",
                                                            "x-description-en": "Translation in progress"
                                                        },
                                                        "to": {
                                                            "format": "date-time",
                                                            "type": "string",
                                                            "x-description-en": "Translation in progress"
                                                        }
                                                    },
                                                    "required": [
                                                        "from",
                                                        "to"
                                                    ],
                                                    "type": "object",
                                                    "x-description-en": "Translation in progress"
                                                }
                                            },
                                            "required": [
                                                "order",
                                                "order_time",
                                                "location_time"
                                            ],
                                            "type": "object",
                                            "x-description-en": "Translation in progress"
                                        },
                                        "type": "array",
                                        "uniqueItems": true,
                                        "x-description-en": "Translation in progress"
                                    },
                                    "key": {
                                        "type": "string",
                                        "x-description-en": "Translation in progress"
                                    },
                                    "trip_time": {
                                        "properties": {
                                            "from": {
                                                "format": "date-time",
                                                "type": "string",
                                                "x-description-en": "Translation in progress"
                                            },
                                            "to": {
                                                "format": "date-time",
                                                "type": "string",
                                                "x-description-en": "Translation in progress"
                                            }
                                        },
                                        "required": [
                                            "from",
                                            "to"
                                        ],
                                        "type": "object",
                                        "x-description-en": "Translation in progress"
                                    },
                                    "waitlist": {
                                        "items": {
                                            "properties": {
                                                "order": {
                                                    "properties": {
                                                        "duration": {
                                                            "format": "float",
                                                            "type": "number",
                                                            "x-description-en": "Translation in progress"
                                                        },
                                                        "facts": {
                                                            "items": {
                                                                "properties": {
                                                                    "time_window": {
                                                                        "properties": {
                                                                            "from": {
                                                                                "format": "date-time",
                                                                                "type": "string",
                                                                                "x-description-en": "Translation in progress"
                                                                            },
                                                                            "to": {
                                                                                "format": "date-time",
                                                                                "type": "string",
                                                                                "x-description-en": "Translation in progress"
                                                                            }
                                                                        },
                                                                        "required": [
                                                                            "from",
                                                                            "to"
                                                                        ],
                                                                        "type": "object",
                                                                        "x-description-en": "Translation in progress"
                                                                    }
                                                                },
                                                                "required": [
                                                                    "time_window"
                                                                ],
                                                                "type": "object",
                                                                "x-description-en": "Translation in progress"
                                                            },
                                                            "maxItems": 100,
                                                            "minItems": 0,
                                                            "type": "array",
                                                            "uniqueItems": true,
                                                            "x-description-en": "Translation in progress"
                                                        },
                                                        "key": {
                                                            "type": "string",
                                                            "x-description-en": "Translation in progress"
                                                        },
                                                        "location": {
                                                            "nullable": true,
                                                            "properties": {
                                                                "arrival_duration": {
                                                                    "default": 0,
                                                                    "format": "int32",
                                                                    "maximum": 1440,
                                                                    "minimum": 0,
                                                                    "type": "integer",
                                                                    "x-description-en": "Translation in progress"
                                                                },
                                                                "departure_duration": {
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
                                                        "reward": {
                                                            "format": "float",
                                                            "type": "number",
                                                            "x-description-en": "Translation in progress"
                                                        },
                                                        "visits": {
                                                            "items": {
                                                                "properties": {
                                                                    "time_window": {
                                                                        "properties": {
                                                                            "from": {
                                                                                "format": "date-time",
                                                                                "type": "string",
                                                                                "x-description-en": "Translation in progress"
                                                                            },
                                                                            "to": {
                                                                                "format": "date-time",
                                                                                "type": "string",
                                                                                "x-description-en": "Translation in progress"
                                                                            }
                                                                        },
                                                                        "required": [
                                                                            "from",
                                                                            "to"
                                                                        ],
                                                                        "type": "object",
                                                                        "x-description-en": "Translation in progress"
                                                                    }
                                                                },
                                                                "required": [
                                                                    "time_window"
                                                                ],
                                                                "type": "object",
                                                                "x-description-en": "Translation in progress"
                                                            },
                                                            "maxItems": 100,
                                                            "minItems": 1,
                                                            "type": "array",
                                                            "uniqueItems": true,
                                                            "x-description-en": "Translation in progress"
                                                        }
                                                    },
                                                    "required": [
                                                        "key",
                                                        "location",
                                                        "visits",
                                                        "duration",
                                                        "reward"
                                                    ],
                                                    "type": "object",
                                                    "x-description-en": "Translation in progress"
                                                }
                                            },
                                            "type": "object"
                                        },
                                        "type": "array",
                                        "uniqueItems": true,
                                        "x-description-en": "Translation in progress"
                                    }
                                },
                                "required": [
                                    "key",
                                    "trip_time"
                                ],
                                "type": "object",
                                "x-description-en": "Translation in progress"
                            },
                            "working_time": {
                                "properties": {
                                    "from": {
                                        "format": "date-time",
                                        "type": "string",
                                        "x-description-en": "Translation in progress"
                                    },
                                    "to": {
                                        "format": "date-time",
                                        "type": "string",
                                        "x-description-en": "Translation in progress"
                                    }
                                },
                                "required": [
                                    "from",
                                    "to"
                                ],
                                "type": "object",
                                "x-description-en": "Translation in progress"
                            }
                        },
                        "required": [
                            "availability_time",
                            "working_time"
                        ],
                        "type": "object",
                        "x-description-en": "Translation in progress"
                    },
                    "maxItems": 100,
                    "minItems": 1,
                    "type": "array",
                    "uniqueItems": true,
                    "x-description-en": "Translation in progress"
                },
                "start_location": {
                    "nullable": true,
                    "properties": {
                        "arrival_duration": {
                            "default": 0,
                            "format": "int32",
                            "maximum": 1440,
                            "minimum": 0,
                            "type": "integer",
                            "x-description-en": "Translation in progress"
                        },
                        "departure_duration": {
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
                "tariff": {
                    "properties": {
                        "basic": {
                            "nullable": true,
                            "properties": {
                                "cost_per_meter": {
                                    "format": "float",
                                    "type": "number",
                                    "x-description-en": "Translation in progress"
                                },
                                "cost_per_minute": {
                                    "format": "float",
                                    "type": "number",
                                    "x-description-en": "Translation in progress"
                                },
                                "cost_per_shift": {
                                    "format": "float",
                                    "type": "number",
                                    "x-description-en": "Translation in progress"
                                },
                                "max_length": {
                                    "format": "float",
                                    "minimum": 1,
                                    "type": "number",
                                    "x-description-en": "Translation in progress"
                                },
                                "max_time": {
                                    "format": "float",
                                    "minimum": 1,
                                    "type": "number",
                                    "x-description-en": "Translation in progress"
                                }
                            },
                            "required": [
                                "cost_per_shift",
                                "cost_per_meter",
                                "max_length",
                                "cost_per_minute",
                                "max_time"
                            ],
                            "type": "object",
                            "x-description-en": "Translation in progress"
                        },
                        "extra": {
                            "items": {
                                "nullable": true,
                                "properties": {
                                    "cost_per_meter": {
                                        "format": "float",
                                        "type": "number",
                                        "x-description-en": "Translation in progress"
                                    },
                                    "cost_per_minute": {
                                        "format": "float",
                                        "type": "number",
                                        "x-description-en": "Translation in progress"
                                    },
                                    "cost_per_shift": {
                                        "format": "float",
                                        "type": "number",
                                        "x-description-en": "Translation in progress"
                                    },
                                    "max_length": {
                                        "format": "float",
                                        "minimum": 1,
                                        "type": "number",
                                        "x-description-en": "Translation in progress"
                                    },
                                    "max_time": {
                                        "format": "float",
                                        "minimum": 1,
                                        "type": "number",
                                        "x-description-en": "Translation in progress"
                                    }
                                },
                                "required": [
                                    "cost_per_shift",
                                    "cost_per_meter",
                                    "max_length",
                                    "cost_per_minute",
                                    "max_time"
                                ],
                                "type": "object",
                                "x-description-en": "Translation in progress"
                            },
                            "maxItems": 10,
                            "minItems": 0,
                            "type": "array",
                            "x-description-en": "Translation in progress"
                        }
                    },
                    "required": [
                        "basic"
                    ],
                    "type": "object",
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
                }
            },
            "required": [
                "key",
                "transport_type",
                "shifts",
                "tariff"
            ],
            "type": "object",
            "x-description-en": "Translation in progress"
        },
        "settings": {
            "properties": {
                "configuration": {
                    "default": "optimize_money",
                    "type": "string",
                    "x-description-en": "Translation in progress"
                },
                "flight_distance": {
                    "default": false,
                    "type": "boolean",
                    "x-description-en": "Translation in progress"
                },
                "planning_time": {
                    "default": 20,
                    "format": "int32",
                    "maximum": 1440,
                    "minimum": 1,
                    "type": "integer",
                    "x-description-en": "Translation in progress"
                },
                "predict_slots": {
                    "default": 0,
                    "format": "int32",
                    "maximum": 4,
                    "minimum": 0,
                    "type": "integer",
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
                "result_ttl": {
                    "default": 20,
                    "format": "int32",
                    "maximum": 1440,
                    "minimum": 1,
                    "type": "integer",
                    "x-description-en": "Translation in progress"
                },
                "routing": {
                    "items": {
                        "properties": {
                            "distance_matrix": {
                                "nullable": true,
                                "properties": {
                                    "distances": {
                                        "items": {
                                            "items": {
                                                "format": "int64",
                                                "type": "integer",
                                                "x-description-en": "Translation in progress"
                                            },
                                            "maxItems": 7000,
                                            "minItems": 2,
                                            "type": "array",
                                            "uniqueItems": false,
                                            "x-description-en": "Translation in progress"
                                        },
                                        "maxItems": 7000,
                                        "minItems": 2,
                                        "type": "array",
                                        "uniqueItems": false,
                                        "x-description-en": "Translation in progress"
                                    },
                                    "durations": {
                                        "items": {
                                            "items": {
                                                "format": "int64",
                                                "type": "integer",
                                                "x-description-en": "Translation in progress"
                                            },
                                            "maxItems": 7000,
                                            "minItems": 2,
                                            "type": "array",
                                            "uniqueItems": false,
                                            "x-description-en": "Translation in progress"
                                        },
                                        "maxItems": 7000,
                                        "minItems": 2,
                                        "type": "array",
                                        "uniqueItems": false,
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
                                    "waypoints",
                                    "distances",
                                    "durations"
                                ],
                                "type": "object",
                                "x-description-en": "Translation in progress"
                            },
                            "traffic_jams": {
                                "items": {
                                    "properties": {
                                        "distance_matrix": {
                                            "nullable": true,
                                            "properties": {
                                                "distances": {
                                                    "items": {
                                                        "items": {
                                                            "format": "int64",
                                                            "type": "integer",
                                                            "x-description-en": "Translation in progress"
                                                        },
                                                        "maxItems": 7000,
                                                        "minItems": 2,
                                                        "type": "array",
                                                        "uniqueItems": false,
                                                        "x-description-en": "Translation in progress"
                                                    },
                                                    "maxItems": 7000,
                                                    "minItems": 2,
                                                    "type": "array",
                                                    "uniqueItems": false,
                                                    "x-description-en": "Translation in progress"
                                                },
                                                "durations": {
                                                    "items": {
                                                        "items": {
                                                            "format": "int64",
                                                            "type": "integer",
                                                            "x-description-en": "Translation in progress"
                                                        },
                                                        "maxItems": 7000,
                                                        "minItems": 2,
                                                        "type": "array",
                                                        "uniqueItems": false,
                                                        "x-description-en": "Translation in progress"
                                                    },
                                                    "maxItems": 7000,
                                                    "minItems": 2,
                                                    "type": "array",
                                                    "uniqueItems": false,
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
                                                "waypoints",
                                                "distances",
                                                "durations"
                                            ],
                                            "type": "object",
                                            "x-description-en": "Translation in progress"
                                        },
                                        "time_window": {
                                            "properties": {
                                                "from": {
                                                    "format": "date-time",
                                                    "type": "string",
                                                    "x-description-en": "Translation in progress"
                                                },
                                                "to": {
                                                    "format": "date-time",
                                                    "type": "string",
                                                    "x-description-en": "Translation in progress"
                                                }
                                            },
                                            "required": [
                                                "from",
                                                "to"
                                            ],
                                            "type": "object",
                                            "x-description-en": "Translation in progress"
                                        }
                                    },
                                    "required": [
                                        "time_window",
                                        "distance_matrix"
                                    ],
                                    "type": "object",
                                    "x-description-en": "Translation in progress"
                                },
                                "maxItems": 24,
                                "minItems": 0,
                                "type": "array",
                                "uniqueItems": true,
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
                            }
                        },
                        "required": [
                            "transport_type",
                            "distance_matrix"
                        ],
                        "type": "object",
                        "x-description-en": "Translation in progress"
                    },
                    "maxItems": 4,
                    "minItems": 0,
                    "type": "array",
                    "uniqueItems": true,
                    "x-description-en": "Translation in progress"
                },
                "traffic_jams": {
                    "default": true,
                    "type": "boolean",
                    "x-description-en": "Translation in progress"
                },
                "transport_factor": {
                    "items": {
                        "properties": {
                            "speed": {
                                "default": 1,
                                "format": "float",
                                "type": "number",
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
                            }
                        },
                        "required": [
                            "transport_type",
                            "speed"
                        ],
                        "type": "object",
                        "x-description-en": "Translation in progress"
                    },
                    "maxItems": 7,
                    "minItems": 0,
                    "type": "array",
                    "uniqueItems": true,
                    "x-description-en": "Translation in progress"
                }
            },
            "type": "object",
            "x-description-en": "Translation in progress"
        }
    },
    "required": [
        "performer",
        "orders"
    ],
    "type": "object",
    "x-description-en": "Translation in progress"
}