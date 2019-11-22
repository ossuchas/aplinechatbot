from ma import ma
from models.crm_line_actual_income import ActualIncomeModel


class ActualIncomeSchema(ma.ModelSchema):
    class Meta:
        model = ActualIncomeModel
