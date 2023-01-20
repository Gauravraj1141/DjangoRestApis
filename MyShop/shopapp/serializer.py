from rest_framework import serializers

# here we give some field of our model here we give field by own


class ProductsSerializer(serializers.Serializer):
    pr_id = serializers.IntegerField()
    product_name = serializers.CharField(max_length=343)
