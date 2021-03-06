from django.db import models
from core.models import CoreModel


class Cue(CoreModel):
    # 큐가 하대인지 상대인지 
    # Serializer로 Validate
    isButt = models.BooleanField(default=False)
    isShaft = models.BooleanField(default=False)

    # 큐 브랜드
    # 모델명
    # 큐의 시리얼 번호, 없으면 빈칸 가능
    productBrand = models.CharField(default=False, max_length=140)
    productName = models.CharField(default=False, max_length=140)
    productNumber = models.CharField(default=False, max_length=140, blank=True)
    
    # 구매 구객
    # 출고일
    purchasedCustomer = models.CharField(max_length=140)
    purchasedCustomerProtectedName = models.CharField(max_length=140, blank=True)
    purchasedDate = models.DateTimeField(auto_now_add=True)
    
    # 보증서 번호 - Serializer에서 자동 생성
    # 보증 기간 - Serializer에서 하대면 1년 상대면 6개월
    # 보증 담당자 
    warrantyNumber = models.CharField(max_length=140, blank=True) 
    warrantyDate = models.DateTimeField(blank=True)
    warrantyManager = models.CharField(max_length=140)
    
    # 조회수
    # 마지막 조회일
    count = models.IntegerField(default=0, blank=True)    
    lastView = models.DateTimeField(blank=True)

    def __str__(self):
        return "보증번호 : " + self.warrantyNumber

    class Meta:
        ordering = ["-pk"]

