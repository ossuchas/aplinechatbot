from ma import ma
from models.crm_line_ll_data import LeadLagModel


class LeadLagSchema(ma.ModelSchema):
    class Meta:
        model = LeadLagModel
