from dynamicfield_serializer import DynamicFieldSerializer
from .utils import replacer, calculate, get_operations


class CalculationDynamicFieldSerializer(DynamicFieldSerializer):
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        calc = self.context.get("calculation")
        if calc:
            calc = get_operations(calc)
            for name, value in ret.items():
                if name in calc:
                    data = replacer(calc[name], ret)
                    ret[fname] = calculate(data)

        return ret
