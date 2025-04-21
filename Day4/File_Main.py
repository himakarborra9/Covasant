from pkg.file import File
import datetime

fs = File(r"C:\Users\Himakar\Desktop\handson")
print(fs.getMaxSizeFile(5))
print(fs.getLatestFiles(datetime.date(2025,4,7)))
