# علیش که جدیدا نمی‌تونه خوب بنویسه، از پاشا می‌خواد که جمله‌ای که تو ذهنش هست رو واسش بنویسه. پاشا هم که می‌خواد استیل بیاد تصمیم می‌گیره که این جمله رو تایپ کنه اما از اون‌جایی که حتی بلد نیست تایپ کنه، وقتی داره جمله رو می‌نویسه به‌جای دکمه بک‌اسپیس(پاک کردن آخرین حرف نوشته شده در صورت وجود) دکمه = رو می‌زنه. (دقت کنید که اگر در ابتدای جمله بک‌اسپیس زده شه هیچ اتفاقی نمی‌افته!) پاشا هم که نمی‌خواد زحماتش حروم بشه و جلوی علیش ضایع بشه از شما کمک می‌خواد و به شما رشته‌ای که تایپ کرده رو میده و ازتون می‌خواد براش رشته اصلی رو بنویسید.
# ورودی
#
# در تنها خط ورودی یک رشته SSS آمده‌است که همان رشته نوشته‌شده توسط پاشا است.
#
# 1≤∣S∣≤100 0001 \le |S| \le 100\ 0001≤∣S∣≤100 000
#
#     رشته SSS تنها از حروف کوچک انگلیسی و = تشکیل شده‌است.
#string slicing is allowed
#input: sall=am
#output :salam


text=input()
output=''
count=0
last=0
for i in range(len(text)):
    if count>0:
        if text[i]=='=':
            count+=1
        else:
            print (i-(count*2))
            output+=text[last:i-(count*2)]
            last=i
            count=0
    else:
        if text[i]=='=':
            count=1
output+=text[last:len(text)-(count*2)]
print (output)
