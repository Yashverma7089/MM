"""MM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import AdminView
from . import EmployeeView
from . import StateCityView
from . import CategoryView
from . import SubCategoryView
from . import ProductView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminlogin/',AdminView.AdminLogin),
    # Employee Urls
    path('employeeinterface/',EmployeeView.EmployeeInterface),
    path('employeesubmit',EmployeeView.EmployeeSubmit),
    path('displayall/',EmployeeView.DisplayAll),
    path('displayemployeebyid/',EmployeeView.DisplayById),
    path('editdeleteemployeerecord/',EmployeeView.EditDeleteRecord),
    path('editemployeepicture/',EmployeeView.EditEmployeePicture),
    path('saveeditpicture',EmployeeView.SaveEditPicture),

    # Category Urls
    path('categoryinterface/',CategoryView.CategoryInterface),
    path('categorysubmit',CategoryView.CategorySubmit),
    path('displayallcategory/',CategoryView.DisplayAllCategory),
    path('displaycategorybyid/',CategoryView.DisplayCategoryById),
    path('editdeletecategoryrecord/',CategoryView.EditDeleteCategoryRecord),
    path('editcategorypicture/',CategoryView.EditCategoryPicture),
    path('saveeditcategorypicture',CategoryView.SaveEditCategoryPicture),
    path('getcategoryjson/',CategoryView.GetCategoryJSON), 
    
    # SubCategory Urls
    path('subcategoryinterface/',SubCategoryView.SubCategoryInterface),
    path('subcategorysubmit',SubCategoryView.SubCategorySubmit),
    path('displayallsubcategory/',SubCategoryView.DisplayAllSubCategory),
    path('displaysubcategorybyid/',SubCategoryView.DisplaySubCategoryById),
    path('editdeletesubcategoryrecord/',SubCategoryView.EditDeleteSubCategoryRecord),
    path('editsubcategorypicture/',SubCategoryView.EditSubCategoryPicture),
    path('saveeditsubcategorypicture',SubCategoryView.SaveEditSubCategoryPicture),
    path('getsubcategoryjson/',SubCategoryView.GetSubCategoryJSON), 

    # Product Urls
    path('productinterface/',ProductView.ProductInterface),
    path('productsubmit',ProductView.ProductSubmit),
    path('displayallproduct/',ProductView.DisplayAllProduct),
    path('displayproductbyid/',ProductView.DisplayProductById),
    path('editdeleteproductrecord/',ProductView.EditDeleteProductRecord),
    path('editproductpicture/',ProductView.EditProductPicture),
    path('saveeditproductpicture',ProductView.SaveEditProductPicture),

    path('fetchallstates/',StateCityView.FetchAllStates),
    path('fetchallcities/',StateCityView.FetchAllCities),
]
