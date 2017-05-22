from rest_framework import serializers, viewsets
from models.models import Employee,Department,OfficeAsset,AssetUseinfo


class DepartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('name','leader')
class OfficeAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficeAsset
        fields = ('asset_type','sn')

class EmpSerializer(serializers.HyperlinkedModelSerializer):
    depart = DepartSerializer()
    asset = OfficeAssetSerializer()
    class Meta:
        model = Employee
        fields = ('name','depart','asset')



class EmpViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmpSerializer
    search_fields = ('name', 'asset__name')


