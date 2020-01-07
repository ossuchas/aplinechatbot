from ma import ma
from models.vw_crm_line_userroleproj import UserRoleProjModel


class UserRoleProjSchema(ma.ModelSchema):
    class Meta:
        model = UserRoleProjModel

