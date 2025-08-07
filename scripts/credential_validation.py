from tencentcloud.common import credential
from tencentcloud.tmt.v20180321 import tmt_client, models

def verify_tencent_translation():
    # 替换为您的密钥（从申请邮件/CAM下载的CSV获取）
    SECRET_ID = "REPLACE_WITH_YOUR_TENCENT_SECRET_ID"  # 占位符 - 请替换为实际密钥
    SECRET_KEY = "REPLACE_WITH_YOUR_TENCENT_SECRET_KEY"    # 占位符 - 请替换为实际密钥

    try:
        # 1. 创建客户端（必须指定广州地域！）
        cred = credential.Credential(SECRET_ID, SECRET_KEY)
        client = tmt_client.TmtClient(cred, "ap-guangzhou")  # 地域必须是 ap-guangzhou

        # 2. 构造请求
        req = models.TextTranslateRequest()
        req.SourceText = "腾讯云翻译服务验证"
        req.Source = "zh"
        req.Target = "en"
        req.ProjectId = 0  # 免费项目固定填0

        # 3. 发送请求
        resp = client.TextTranslate(req)

        # 4. 验证结果
        if "Translation" in str(resp):
            print("✅ 验证成功！密钥有效且可访问翻译服务")
            print("测试翻译结果:", resp.TargetText)
            print("👉 您的免费额度已生效，可安全用于博客翻译")
            return True
        else:
            print("❌ 翻译结果异常:", resp)
            return False
            
    except Exception as e:
        print("🔥 验证失败！错误详情:")
        if "AuthFailure" in str(e):
            print("  → 权限错误：检查子账号是否授权 TMT_QcsRole 策略")
        elif "InvalidParameterValue" in str(e):
            print("  → 参数错误：检查地域是否为 ap-guangzhou")
        else:
            print("  → 未知错误:", str(e))
        return False

# 执行验证
if __name__ == "__main__":
    verify_tencent_translation()
