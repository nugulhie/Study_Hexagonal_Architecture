from django.db import models

# Create your models here.
class Users(models.Model):
    uuid = models.CharField(primary_key=True)
    createdat = models.DateTimeField(db_column="created_at", auto_now_add=True)
    updatedat = models.DateTimeField(db_column="updated_at", auto_now=True)

class PartnerSettlementInfo(models.Model):
    business_number = models.CharField(max_length=120, null=True, help_text="사업자 등록 번호")
    ceo_name = models.CharField(max_length=120, null=True, help_text="대표자 이름")
    representative_number = models.CharField(max_length=20, help_text="대표번호")
    phone_number = models.CharField(max_length=20, help_text="대표자 전화번호", null=True)
    representative_email = models.EmailField(help_text="대표자 이메일")
    account_depositor = models.CharField(max_length=20, help_text="정산 계좌 예금주 이름")
    account_number = models.CharField(max_length=20, help_text="정산 계좌번호")
    bank_code = models.CharField(max_length=10, help_text="정산 계좌 은행코드")
    account_type = models.CharField(
        max_length=20, default="INDIVIDUAL", help_text="정산 계좌종류"
    )
    partner = models.ForeignKey(Users, models.DO_NOTHING, db_column="partner_id")
    index = models.AutoField(primary_key=True)
    createdat = models.DateTimeField(db_column="created_at", auto_now_add=True)
    updatedat = models.DateTimeField(db_column="updated_at", auto_now=True)

    class Meta:
        managed = True
        db_table = "partner_settlement_info"
