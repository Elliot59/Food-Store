from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'password')

        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDetail
        exclude = ['id']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['in_stock']

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        addOnes_data = validated_data.pop('addOnes')
        make, created = Product.objects.update_or_create(category=category_data, addOnes=addOnes_data,
                                                         img=validated_data.pop('img'), name=validated_data.pop('name'),
                                                         price=validated_data.pop('price'))
        return make


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = Order
        fields = ['id', 'user', 'products', 'customer', 'orderTime', 'get_add_ones']

    def create(self, validated_data):
        customer_data = validated_data.pop('customer')
        customer = CustomerSerializer.create(CustomerSerializer(), validated_data=customer_data)
        order, created = Order.objects.update_or_create(
            products=validated_data.pop('products'),
            user=validated_data.pop('user'),
            customer=customer,
            get_add_ones=validated_data.pop('get_add_ones')
        )
        return order

    def update(self, instance, validated_data):
        nested_serializer = self.fields['customer']
        nested_instance = instance.customer
        nested_data = validated_data.pop('customer')
        nested_serializer.update(nested_instance, nested_data)
        return super(OrderSerializer, self).update(instance, validated_data)
