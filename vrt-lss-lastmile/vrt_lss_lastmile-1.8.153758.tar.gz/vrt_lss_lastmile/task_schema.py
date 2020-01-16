{
    "properties": {
        "hardlinks": {
            "items": {
                "properties": {
                    "key": {
                        "type": "string",
                        "x-description-en": "Translation in progress"
                    },
                    "links": {
                        "items": {
                            "properties": {
                                "entity_key": {
                                    "type": "string",
                                    "x-description-en": "Translation in progress"
                                },
                                "type": {
                                    "enum": [
                                        "LET_ORDER",
                                        "LET_SHIFT"
                                    ],
                                    "type": "string",
                                    "x-description-en": "Translation in progress"
                                }
                            },
                            "required": [
                                "type",
                                "entity_key"
                            ],
                            "type": "object",
                            "x-description-en": "Translation in progress"
                        },
                        "type": "array",
                        "x-description-en": "Translation in progress"
                    }
                },
                "required": [
                    "key",
                    "links"
                ],
                "type": "object",
                "x-description-en": "Translation in progress"
            },
            "maxItems": 1000,
            "minItems": 0,
            "type": "array",
            "x-description-en": "Translation in progress"
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
                    "key": {
                        "type": "string",
                        "x-description-en": "Translation in progress"
                    },
                    "latitude": {
                        "format": "float",
                        "maximum": 90,
                        "minimum": -90,
                        "type": "number",
                        "x-description-en": "Translation in progress"
                    },
                    "load_windows": {
                        "items": {
                            "properties": {
                                "gates_count": {
                                    "default": 0,
                                    "format": "int32",
                                    "type": "integer",
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
                            "type": "object",
                            "x-description-en": "Translation in progress"
                        },
                        "type": "array",
                        "x-description-en": "Translation in progress"
                    },
                    "longitude": {
                        "format": "float",
                        "maximum": 180,
                        "minimum": -180,
                        "type": "number",
                        "x-description-en": "Translation in progress"
                    },
                    "transport_restrictions": {
                        "items": {
                            "type": "string"
                        },
                        "type": "array",
                        "x-description-en": "Translation in progress"
                    }
                },
                "required": [
                    "key",
                    "latitude",
                    "longitude"
                ],
                "type": "object",
                "x-description-en": "Translation in progress"
            },
            "maxItems": 7000,
            "minItems": 1,
            "type": "array",
            "x-description-en": "Translation in progress"
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
                        "uniqueItems": true,
                        "x-description-en": "Translation in progress"
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
                                    "type": "string",
                                    "x-description-en": "Translation in progress"
                                },
                                "key": {
                                    "type": "string",
                                    "x-description-en": "Translation in progress"
                                },
                                "possible_events": {
                                    "items": {
                                        "properties": {
                                            "duration": {
                                                "format": "int32",
                                                "type": "integer",
                                                "x-description-en": "Translation in progress"
                                            },
                                            "location_key": {
                                                "type": "string",
                                                "x-description-en": "Translation in progress"
                                            },
                                            "reward": {
                                                "format": "float",
                                                "type": "number",
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
                                            "location_key",
                                            "duration",
                                            "time_window"
                                        ],
                                        "type": "object",
                                        "x-description-en": "Translation in progress"
                                    },
                                    "maxItems": 10,
                                    "minItems": 1,
                                    "type": "array",
                                    "uniqueItems": true,
                                    "x-description-en": "Translation in progress"
                                },
                                "precedence_in_order": {
                                    "default": 0,
                                    "format": "int32",
                                    "type": "integer",
                                    "x-description-en": "Translation in progress"
                                },
                                "precedence_in_trip": {
                                    "default": 0,
                                    "format": "int32",
                                    "type": "integer",
                                    "x-description-en": "Translation in progress"
                                },
                                "target_cargos": {
                                    "items": {
                                        "type": "string"
                                    },
                                    "maxItems": 100,
                                    "minItems": 0,
                                    "type": "array",
                                    "uniqueItems": true,
                                    "x-description-en": "Translation in progress"
                                }
                            },
                            "required": [
                                "key",
                                "demand_type",
                                "possible_events"
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
                    "key": {
                        "type": "string",
                        "x-description-en": "Translation in progress"
                    },
                    "order_features": {
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
                    "order_restrictions": {
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
                    "performer_restrictions": {
                        "items": {
                            "type": "string",
                            "x-description-en": "Translation in progress"
                        },
                        "maxItems": 100,
                        "minItems": 0,
                        "type": "array",
                        "uniqueItems": true,
                        "x-description-en": "Translation in progress"
                    }
                },
                "required": [
                    "key",
                    "demands"
                ],
                "type": "object",
                "x-description-en": "Translation in progress"
            },
            "maxItems": 7000,
            "minItems": 1,
            "type": "array",
            "x-description-en": "Translation in progress"
        },
        "performers": {
            "items": {
                "properties": {
                    "key": {
                        "type": "string",
                        "x-description-en": "Translation in progress"
                    },
                    "max_work_shifts": {
                        "format": "int32",
                        "type": "integer",
                        "x-description-en": "Translation in progress"
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
                            "type": "string",
                            "x-description-en": "Translation in progress"
                        },
                        "type": "array",
                        "x-description-en": "Translation in progress"
                    },
                    "transport_restrictions": {
                        "items": {
                            "type": "string",
                            "x-description-en": "Translation in progress"
                        },
                        "type": "array",
                        "x-description-en": "Translation in progress"
                    }
                },
                "required": [
                    "key"
                ],
                "type": "object",
                "x-description-en": "Translation in progress"
            },
            "maxItems": 7000,
            "minItems": 1,
            "type": "array",
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
                        "type": "string",
                        "x-description-en": "Translation in progress"
                    },
                    "key": {
                        "type": "string",
                        "x-description-en": "Translation in progress"
                    },
                    "resource_key": {
                        "type": "string",
                        "x-description-en": "Translation in progress"
                    },
                    "shift_type": {
                        "enum": [
                            "ST_PERFORMER",
                            "ST_TRANSPORT"
                        ],
                        "type": "string",
                        "x-description-en": "Translation in progress"
                    },
                    "start_location_key": {
                        "type": "string",
                        "x-description-en": "Translation in progress"
                    },
                    "tariff": {
                        "properties": {
                            "constraints": {
                                "items": {
                                    "properties": {
                                        "cost_per_unit": {
                                            "format": "float",
                                            "type": "number",
                                            "x-description-en": "Translation in progress"
                                        },
                                        "stage_length": {
                                            "format": "float",
                                            "type": "number",
                                            "x-description-en": "Translation in progress"
                                        }
                                    },
                                    "required": [
                                        "stage_length",
                                        "cost_per_unit"
                                    ],
                                    "type": "object",
                                    "x-description-en": "Translation in progress"
                                },
                                "type": "array",
                                "x-description-en": "Translation in progress"
                            },
                            "cost_per_shift": {
                                "format": "float",
                                "type": "number",
                                "x-description-en": "Translation in progress"
                            }
                        },
                        "required": [
                            "cost_per_shift",
                            "constraints"
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
                    "key",
                    "shift_type",
                    "resource_key",
                    "availability_time",
                    "working_time",
                    "tariff"
                ],
                "type": "object",
                "x-description-en": "Translation in progress"
            },
            "maxItems": 7000,
            "minItems": 1,
            "type": "array",
            "x-description-en": "Translation in progress"
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
                        "type": "array",
                        "x-description-en": "Translation in progress"
                    },
                    "key": {
                        "type": "string",
                        "x-description-en": "Translation in progress"
                    },
                    "performer_restrictions": {
                        "items": {
                            "type": "string",
                            "x-description-en": "Translation in progress"
                        },
                        "type": "array",
                        "x-description-en": "Translation in progress"
                    },
                    "transport_features": {
                        "items": {
                            "type": "string",
                            "x-description-en": "Translation in progress"
                        },
                        "type": "array",
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
                    "key"
                ],
                "type": "object",
                "x-description-en": "Translation in progress"
            },
            "maxItems": 7000,
            "minItems": 1,
            "type": "array",
            "x-description-en": "Translation in progress"
        }
    },
    "required": [
        "locations",
        "orders",
        "performers",
        "transports",
        "shifts"
    ],
    "type": "object",
    "x-description-en": "Translation in progress"
}