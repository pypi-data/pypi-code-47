{
    "properties": {
        "hardlinks": {
            "items": {
                "properties": {
                    "key": {
                        "type": "string"
                    },
                    "links": {
                        "items": {
                            "properties": {
                                "entity_key": {
                                    "type": "string"
                                },
                                "type": {
                                    "enum": [
                                        "LET_ORDER",
                                        "LET_SHIFT"
                                    ],
                                    "type": "string"
                                }
                            },
                            "required": [
                                "type",
                                "entity_key"
                            ],
                            "type": "object"
                        },
                        "type": "array"
                    }
                },
                "required": [
                    "key",
                    "links"
                ],
                "type": "object"
            },
            "maxItems": 1000,
            "minItems": 0,
            "type": "array"
        },
        "locations": {
            "items": {
                "nullable": true,
                "properties": {
                    "arrival_duration": {
                        "default": 0,
                        "format": "int32",
                        "maximum": 1440,
                        "minimum": 0,
                        "type": "integer"
                    },
                    "departure_duration": {
                        "default": 0,
                        "format": "int32",
                        "maximum": 1440,
                        "minimum": 0,
                        "type": "integer"
                    },
                    "key": {
                        "type": "string"
                    },
                    "latitude": {
                        "format": "float",
                        "maximum": 90,
                        "minimum": -90,
                        "type": "number"
                    },
                    "load_windows": {
                        "items": {
                            "properties": {
                                "gates_count": {
                                    "default": 0,
                                    "format": "int32",
                                    "type": "integer"
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
                            "type": "object"
                        },
                        "type": "array"
                    },
                    "longitude": {
                        "format": "float",
                        "maximum": 180,
                        "minimum": -180,
                        "type": "number"
                    },
                    "transport_restrictions": {
                        "items": {
                            "type": "string"
                        },
                        "type": "array"
                    }
                },
                "required": [
                    "key",
                    "latitude",
                    "longitude"
                ],
                "type": "object"
            },
            "maxItems": 7000,
            "minItems": 1,
            "type": "array"
        },
        "orders": {
            "items": {
                "nullable": true,
                "properties": {
                    "cargos": {
                        "items": {
                            "nullable": true,
                            "properties": {
                                "capacity_x": {
                                    "default": 0,
                                    "format": "float",
                                    "type": "number",
                                    "x-description-en": "Translation in progress"
                                },
                                "capacity_y": {
                                    "default": 0,
                                    "format": "float",
                                    "type": "number",
                                    "x-description-en": "Translation in progress"
                                },
                                "capacity_z": {
                                    "default": 0,
                                    "format": "float",
                                    "type": "number",
                                    "x-description-en": "Translation in progress"
                                },
                                "height": {
                                    "default": 0,
                                    "format": "float",
                                    "type": "number",
                                    "x-description-en": "Translation in progress"
                                },
                                "key": {
                                    "type": "string",
                                    "x-description-en": "Translation in progress"
                                },
                                "length": {
                                    "default": 0,
                                    "format": "float",
                                    "type": "number",
                                    "x-description-en": "Translation in progress"
                                },
                                "mass": {
                                    "default": 1,
                                    "format": "float",
                                    "type": "number",
                                    "x-description-en": "Translation in progress"
                                },
                                "max_storage_time": {
                                    "format": "int32",
                                    "type": "integer",
                                    "x-description-en": "Translation in progress"
                                },
                                "restrictions": {
                                    "items": {
                                        "type": "string",
                                        "x-description-en": "Translation in progress"
                                    },
                                    "maxItems": 100,
                                    "minItems": 0,
                                    "type": "array",
                                    "uniqueItems": true,
                                    "x-description-en": "Translation in progress"
                                },
                                "volume": {
                                    "default": 0,
                                    "format": "float",
                                    "type": "number",
                                    "x-description-en": "Translation in progress"
                                },
                                "width": {
                                    "default": 0,
                                    "format": "float",
                                    "type": "number",
                                    "x-description-en": "Translation in progress"
                                }
                            },
                            "required": [
                                "key",
                                "mass"
                            ],
                            "type": "object",
                            "x-description-en": "Translation in progress"
                        },
                        "maxItems": 100,
                        "minItems": 0,
                        "type": "array",
                        "uniqueItems": true
                    },
                    "demands": {
                        "items": {
                            "nullable": true,
                            "properties": {
                                "demand_type": {
                                    "enum": [
                                        "DT_PICKUP",
                                        "DT_DROP",
                                        "DT_WORK"
                                    ],
                                    "type": "string"
                                },
                                "key": {
                                    "type": "string"
                                },
                                "possible_events": {
                                    "items": {
                                        "properties": {
                                            "duration": {
                                                "format": "int32",
                                                "type": "integer"
                                            },
                                            "location_key": {
                                                "type": "string"
                                            },
                                            "reward": {
                                                "format": "float",
                                                "type": "number"
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
                                            "location_key",
                                            "duration",
                                            "time_window"
                                        ],
                                        "type": "object"
                                    },
                                    "maxItems": 10,
                                    "minItems": 1,
                                    "type": "array",
                                    "uniqueItems": true
                                },
                                "precedence_in_order": {
                                    "default": 0,
                                    "format": "int32",
                                    "type": "integer"
                                },
                                "precedence_in_trip": {
                                    "default": 0,
                                    "format": "int32",
                                    "type": "integer"
                                },
                                "target_cargos": {
                                    "items": {
                                        "type": "string"
                                    },
                                    "maxItems": 100,
                                    "minItems": 0,
                                    "type": "array",
                                    "uniqueItems": true
                                }
                            },
                            "required": [
                                "key",
                                "demand_type",
                                "possible_events"
                            ],
                            "type": "object"
                        },
                        "maxItems": 100,
                        "minItems": 1,
                        "type": "array",
                        "uniqueItems": true
                    },
                    "key": {
                        "type": "string"
                    },
                    "order_features": {
                        "items": {
                            "type": "string"
                        },
                        "maxItems": 100,
                        "minItems": 0,
                        "type": "array",
                        "uniqueItems": true
                    },
                    "order_restrictions": {
                        "items": {
                            "type": "string"
                        },
                        "maxItems": 100,
                        "minItems": 0,
                        "type": "array",
                        "uniqueItems": true
                    },
                    "performer_restrictions": {
                        "items": {
                            "type": "string"
                        },
                        "maxItems": 100,
                        "minItems": 0,
                        "type": "array",
                        "uniqueItems": true
                    }
                },
                "required": [
                    "key",
                    "demands"
                ],
                "type": "object"
            },
            "maxItems": 7000,
            "minItems": 1,
            "type": "array"
        },
        "performers": {
            "items": {
                "properties": {
                    "key": {
                        "type": "string"
                    },
                    "max_work_shifts": {
                        "format": "int32",
                        "type": "integer"
                    },
                    "own_transport_type": {
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
                    "performer_features": {
                        "items": {
                            "type": "string"
                        },
                        "type": "array"
                    },
                    "transport_restrictions": {
                        "items": {
                            "type": "string"
                        },
                        "type": "array"
                    }
                },
                "required": [
                    "key"
                ],
                "type": "object"
            },
            "maxItems": 7000,
            "minItems": 1,
            "type": "array"
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
                    "finish_location_key": {
                        "type": "string"
                    },
                    "key": {
                        "type": "string"
                    },
                    "resource_key": {
                        "type": "string"
                    },
                    "shift_type": {
                        "enum": [
                            "ST_PERFORMER",
                            "ST_TRANSPORT"
                        ],
                        "type": "string"
                    },
                    "start_location_key": {
                        "type": "string"
                    },
                    "tariff": {
                        "properties": {
                            "constraints": {
                                "items": {
                                    "properties": {
                                        "cost_per_unit": {
                                            "format": "float",
                                            "type": "number"
                                        },
                                        "stage_length": {
                                            "format": "float",
                                            "type": "number"
                                        }
                                    },
                                    "required": [
                                        "stage_length",
                                        "cost_per_unit"
                                    ],
                                    "type": "object"
                                },
                                "type": "array"
                            },
                            "cost_per_shift": {
                                "format": "float",
                                "type": "number"
                            }
                        },
                        "required": [
                            "cost_per_shift",
                            "constraints"
                        ],
                        "type": "object"
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
                    "key",
                    "shift_type",
                    "resource_key",
                    "availability_time",
                    "working_time",
                    "tariff"
                ],
                "type": "object"
            },
            "maxItems": 7000,
            "minItems": 1,
            "type": "array"
        },
        "transports": {
            "items": {
                "properties": {
                    "boxes": {
                        "items": {
                            "nullable": true,
                            "properties": {
                                "capacity_x": {
                                    "default": 0,
                                    "format": "float",
                                    "type": "number",
                                    "x-description-en": "Translation in progress"
                                },
                                "capacity_y": {
                                    "default": 0,
                                    "format": "float",
                                    "type": "number",
                                    "x-description-en": "Translation in progress"
                                },
                                "capacity_z": {
                                    "default": 0,
                                    "format": "float",
                                    "type": "number",
                                    "x-description-en": "Translation in progress"
                                },
                                "features": {
                                    "items": {
                                        "type": "string",
                                        "x-description-en": "Translation in progress"
                                    },
                                    "maxItems": 100,
                                    "minItems": 0,
                                    "type": "array",
                                    "uniqueItems": true,
                                    "x-description-en": "Translation in progress"
                                },
                                "height": {
                                    "default": 0,
                                    "format": "float",
                                    "type": "number",
                                    "x-description-en": "Translation in progress"
                                },
                                "key": {
                                    "type": "string",
                                    "x-description-en": "Translation in progress"
                                },
                                "length": {
                                    "default": 0,
                                    "format": "float",
                                    "type": "number",
                                    "x-description-en": "Translation in progress"
                                },
                                "mass": {
                                    "default": 100,
                                    "format": "float",
                                    "type": "number",
                                    "x-description-en": "Translation in progress"
                                },
                                "volume": {
                                    "default": 100,
                                    "format": "float",
                                    "type": "number",
                                    "x-description-en": "Translation in progress"
                                },
                                "width": {
                                    "default": 0,
                                    "format": "float",
                                    "type": "number",
                                    "x-description-en": "Translation in progress"
                                }
                            },
                            "required": [
                                "mass"
                            ],
                            "type": "object",
                            "x-description-en": "Translation in progress"
                        },
                        "type": "array"
                    },
                    "key": {
                        "type": "string"
                    },
                    "performer_restrictions": {
                        "items": {
                            "type": "string"
                        },
                        "type": "array"
                    },
                    "transport_features": {
                        "items": {
                            "type": "string"
                        },
                        "type": "array"
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
                    "key"
                ],
                "type": "object"
            },
            "maxItems": 7000,
            "minItems": 1,
            "type": "array"
        }
    },
    "required": [
        "locations",
        "orders",
        "performers",
        "transports",
        "shifts"
    ],
    "type": "object"
}