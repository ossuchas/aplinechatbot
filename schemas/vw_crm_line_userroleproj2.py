from ma import ma
from models.vw_crm_line_userroleproj import UserRoleProjModel


class UserRoleProj2Schema(ma.ModelSchema):
    class Meta:
        model = UserRoleProjModel
        fields = ("display_project", )

