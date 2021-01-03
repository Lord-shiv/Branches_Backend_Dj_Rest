from rest_framework import viewsets, generics
# from rest_framework.filters import SearchFilter, OrderingFilter
# from rest_framework import filters
from rest_framework.response import Response
from branches.models import Branch
from branches.serializers import BranchSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


# class BranchListView(viewsets.ModelViewSet):
#     queryset = Branch.objects.all().order_by('-ifsc_code')
#     serializer_class = BranchSerializer
#     filter_backends = (SearchFilter, filters.OrderingFilter)
#     search_fields = ('branch_name', 'ifsc_code', 'city', 'state', 'district')
#     ordering_fields = ['branch_name', 'ifsc_code', 'city', 'state', 'district']


@csrf_exempt
def BranchesApi(request, id=0):
    if request.method == 'GET':
        branches = Branch.objects.all()
        branch_serializer = BranchSerializer(branches, many=True)
        return JsonResponse(branch_serializer.data, safe=False)

    elif request.method == 'POST':
        branch_data = JSONParser().parse(request)
        branch_serializer = BranchSerializer(data=branch_data)
        if branch_serializer.is_valid():
            branch_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method == 'PUT':
        branch_data = JSONParser().parse(request)
        branch = Branch.objects.get(branchId=branch_data['branchId'])
        branch_serializer = BranchSerializer(branch, data=branch_data)
        if branch_serializer.is_valid():
            branch_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method == 'DELETE':
        branch = Branch.objects.get(branchId=id)
        branch.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)
