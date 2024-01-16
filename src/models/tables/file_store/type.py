from enum import Enum
from typing import Any, Optional
# from pydantic import BaseModel, Field
from sqlmodel import SQLModel, Field 
from models.common.company_info.type import CompanyInfo, CompanyInfoFilter
from models.common.filter_params.type import FilterParams

from models.common.id.type import ID, IDFilter
from models.common.priority.type import Priority
from models.common.record.type import Record
from models.common.status.type import Status


class FileStoreBase(ID, SQLModel):
    file_name : str = Field(...,index=True)
    file_path : str = Field(...,)
    file_size : int = Field(...,index=True)
    file_type : str = Field(...,index=True)
    file_hash : str = Field(...,index=True)
    file_extension : Optional[str] = Field(...)
    
    class config:
        use_enum_values = True  # 配置 Pydantic 使用枚举的值
    pass


class FileStore(FileStoreBase,table=True):
    class config:
        use_enum_values = True  # 配置 Pydantic 使用枚举的值
        

class FileStoreFilterParams(IDFilter,FilterParams,SQLModel):
    file_name : Optional[str] = Field(...,index=True)
    file_size : Optional[int] = Field(...,index=True)
    file_type : Optional[str] = Field(...,index=True)
    file_hash : Optional[str] = Field(...,index=True)
    

    def build_sql_query(self)-> tuple[str,list[Any]]:
        
        sql_fragments = []
        args = []

        # 添加来自其他过滤器的 SQL 片段和参数
        for filter_cls in [ IDFilter]:
            sql_fragment, filter_args = filter_cls.build_sql_query(self) # type: ignore
            sql_fragments.append(sql_fragment)
            args.extend(filter_args)
            
        field_to_sql = {
            "file_name": "file_name LIKE %s",
            "file_size": "file_size = %s",
            "file_type": "file_type = %s",
            "file_hash": "file_hash = %s"
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
    