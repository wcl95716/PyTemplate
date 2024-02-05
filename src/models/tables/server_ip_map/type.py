from enum import Enum
from typing import Any, Optional
# from pydantic import BaseModel, Field
from sqlmodel import SQLModel, Field 
from models.common.filter_params.type import FilterParams

from models.common.id.type import ID, IDFilter
from models.common.update_time.type import UpdateTime


class ServerIPMapBase(ID,UpdateTime, SQLModel):
    server_name: Optional[str] = Field(None, index=True)
    server_ipv4: Optional[str] = Field(None, index=True)
    server_ipv6: Optional[str] = Field(None, index=True)
    server_mac_address: Optional[str] = Field(None, index=True)
    server_user: Optional[str] = Field(None, index=True)
    server_password: Optional[str] = Field(None)
    
    
    class config:
        use_enum_values = True  # 配置 Pydantic 使用枚举的值
    pass


class ServerIPMap(ServerIPMapBase,extend_existing=True ,table=True):
    class config:
        use_enum_values = True  # 配置 Pydantic 使用枚举的值
        

class ServerIPMapParams(IDFilter,FilterParams,SQLModel):
    server_name: Optional[str] = Field(None, index=True)
    server_ipv4: Optional[str] = Field(None, index=True)
    server_ipv6: Optional[str] = Field(None, index=True)
    server_mac_address: Optional[str] = Field(None, index=True)
    server_user: Optional[str] = Field(None, index=True)
    server_password: Optional[str] = Field(None)

    def build_sql_query(self)-> tuple[str,list[Any]]:
        
        sql_fragments = []
        args = []

        # 添加来自其他过滤器的 SQL 片段和参数
        for filter_cls in [ IDFilter]:
            sql_fragment, filter_args = filter_cls.build_sql_query(self) # type: ignore
            sql_fragments.append(sql_fragment)
            args.extend(filter_args)
            
        field_to_sql = {
            "server_name": "server_name LIKE %s",
            "server_ipv4": "server_ipv4 = %s",
            "server_ipv6": "server_ipv6 = %s",
            "server_mac_address": "server_mac_address = %s",
            "server_user": "server_user = %s",
            "server_password": "server_password = %s"
        }
        
                # 生成 SQL 片段和参数
        for field, sql in field_to_sql.items():
            value = getattr(self, field)
            if value is not None:
                # 如果是枚举 则使用 value 属性  如果value 是 None 则跳过
                if isinstance(value, Enum) and value.value == "None":
                    continue
                sql_fragments.append(" AND " + sql)
                
                args.append(str(value.value) if hasattr(value, "value") else value)
        
        sql =  " ".join(sql_fragments)
        
        return sql,args
        pass
    
    
    pass 
    