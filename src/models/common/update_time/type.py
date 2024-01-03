from datetime import datetime, timedelta
from typing import Any, Dict, Optional
import pytz
from sqlalchemy import func

from sqlmodel import SQLModel, Field 


# def convert_to_beijing_time(utc_time: datetime) -> datetime:
#     beijing_tz = pytz.timezone("Asia/Shanghai")
#     return utc_time.astimezone(beijing_tz)


class UpdateTime(SQLModel,extend_existing=True):
    create_time: Optional[datetime] = Field(None, description="数据库自动生成",sa_column_kwargs={"nullable": False, "server_default": func.now()})
    update_time: Optional[datetime] = Field(None, description="更新时间 数据库自动生成",sa_column_kwargs={"nullable": False, "server_default": func.now(), "onupdate": func.now()})

    def __init__(self, **data: Any):
        super().__init__(**data)
        print("UpdateTime __init__" , self.create_time , self.update_time , type(self.create_time) , type(self.update_time))
        # 切换成北京时间
        if self.create_time is not None:
            self.create_time = self.create_time + timedelta(hours=8)
            # print("UpdateTime __init__222 " , self.create_time , self.update_time , type(self.create_time) , type(self.update_time))
        if self.update_time is not None:
            self.update_time = self.update_time + timedelta(hours=8)
            
    @property
    def create_time_str(self) -> Optional[str]:
        return self.create_time.strftime("%Y-%m-%d %H:%M:%S") if self.create_time is not None else None

    @property
    def update_time_str(self) -> Optional[str]:
        return self.update_time.strftime("%Y-%m-%d %H:%M:%S") if self.update_time is not None else None
    
    def model_dump(self, *, mode: str = 'json', exclude: set[str] = None, include: set[str] = None, by_alias: bool = True, exclude_unset: bool = False, exclude_defaults: bool = False, exclude_none: bool = False, round_trip: bool = False, warnings: bool = True) -> dict[str, Any]:# type: ignore
        data = super().model_dump(mode=mode, exclude=exclude, include=include, by_alias=by_alias, exclude_unset=exclude_unset, exclude_defaults=exclude_defaults, exclude_none=exclude_none, round_trip=round_trip, warnings=warnings)
        
        if self.create_time is not None:
            data["create_time"] = self.create_time.strftime("%Y-%m-%d %H:%M:%S")
        if self.update_time is not None:
            data["update_time"] = self.update_time.strftime("%Y-%m-%d %H:%M:%S")
        
        return data