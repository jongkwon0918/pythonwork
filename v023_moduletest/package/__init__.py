from .calc_tools import salary_prediction,get_vat
from .data_tools import get_today_str,is_weekend
from .security_tools import mask_name, mask_phone
# 패키지에서 제공할 메소드를 설정하기 -> 가이드
# import했을때 * -> 아래 설정내용대로 가져옴
# 직접 import해버리면 사용이 가능
__all__=["salary_prediction","get_today_str","mask_name"]