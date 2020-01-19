from typing import Dict, List, Tuple


def get_real_table_comment(mysql_dict: Dict, table_comment: str) -> str:
    """
    :param mysql_dict:
    :param table_comment:
    :return: 当表注释不为空时返回表注释；否则把主键注释当作表注释
    """
    if table_comment:
        return table_comment
    primary_key_comment: str = list(mysql_dict.values())[0][1]
    if primary_key_comment.upper().strip().endswith('ID'):
        return primary_key_comment[:-2]
    else:
        return primary_key_comment


def get_fields(mysql_dict: Dict[str, Tuple[str, str]]) -> List[Tuple[str, str, str]]:
    """
    :param: mysql_dict
    :return: [(name, java_type, comment)]
    """
    type_map = {
        'varchar': 'String',
        'text': 'String',
        'json': 'JSONObject',
        'datetime': 'LocalDateTime',
        'timestamp': 'LocalDateTime',
        'date': 'LocalDate',
        'time': 'LocalTime',
        'double': 'Double',
        'int': 'Integer',
        'tinyint': 'Integer',
    }
    ret = []
    for name, (sql_type, comment) in mysql_dict.items():
        sql_type = sql_type.lower()
        java_type = type_map.get(sql_type, sql_type.capitalize())
        ret.append((name, java_type, comment))
    return ret


def from_model_tpl(package_root, modelname, tablename, mysql_dict: Dict, table_comment: str):
    def make_field(name, java_type, comment):
        return f"""    @ApiModelProperty(value = "{comment}")\n    private {java_type} {name};\n\n"""

    fields = get_fields(mysql_dict)
    return f"""package {package_root}.entity;

import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;
import lombok.experimental.Accessors;
import tk.mybatis.mapper.annotation.KeySql;
import javax.persistence.Id;
import javax.persistence.Table;
import java.time.LocalDateTime;
import org.json.JSONObject;

@Data
@Accessors(chain = true)
@Table(name = "{tablename}")
@ApiModel(description = "{table_comment}")
public class {modelname} {{

    @Id
    @KeySql(useGeneratedKeys = true)\n{''.join(
        make_field(name, java_type, comment) for (name, java_type, comment) in fields
    )}
}}\n"""


def from_mapper_xml_tpl(package_root, modelname):
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="{package_root}.mapper.{modelname}Mapper">

</mapper>\n"""


def from_mapper_tpl(package_root, modelname) -> str:
    return f"""package {package_root}.mapper;

import {package_root}.entity.{modelname};
import com.parsec.universal.dao.TKMapper;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface {modelname}Mapper extends TKMapper<{modelname}> {{
}}\n"""
