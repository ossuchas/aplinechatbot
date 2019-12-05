from ma import ma
from models.crm_line_exct_report import ExecutiveReportModel


class ExecutiveReportSchema(ma.ModelSchema):
    class Meta:
        model = ExecutiveReportModel
