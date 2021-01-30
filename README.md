<h1 align="center">Phân tích cú pháp cấu trúc ngữ đoạn bằng thuật toán CKY</h1>
Đồ án thực hiện phân tích cú pháp cấu trúc ngữ đoạn trong tiếng Việt.<br/>
Sử dụng thuật toán Maxinum Matching để tách từ. Sau đó dùng thuật toán CKY để phân tích cú pháp. 

## Demo
<p align="center">
  <img width="700" align="center" src="demo.gif"/>
</p>

## Request
Python phiên bản >= 3.6
```sh
sudo apt install python3
```

## Install
Option 1: Dùng git clone repo về
```sh
git clone https://github.com/UITTrinhQuangTruong/CS221.L11.git
```

Option 2: Tải trực tiếp trên trang github này

## Usage
### Tôi muốn phân tích cú pháp từ bộ sentence sẵn có thì sao?
Đơn giản chỉ cần chạy
```sh
python3 main.py
```

### Tôi muốn in toàn bộ kết quả tìm được thì sao?
Thêm cờ -x vào lệnh bash
```sh
python3 main.py -x
```

### Tôi muốn nhập từ bàn phím n câu bất kì thì sao?
Thêm cờ -n vào lệnh bash
```sh
python3 main.py -n
```

### Tôi muốn sử dụng thuật toán tách từ khác thì sao?
Hiện tại, ngoài thuật toán Maximum Matching, chúng tôi còn có sử dụng thêm thư viện VnCoreNLP để tách từ. Để sử dụng thư viện, chạy lệnh
```sh
python3 main.py -vn
```

### Tôi muốn sử dụng mô hình phân tích cú pháp khác thì sao?
Có thể chứ,chúng tôi cung cấp thêm cả phân tích cú pháp của StandfordCoreNLP, để thực hiện điều đó, trước tiên cần cài đặt StandfordCoreNLP, [tham khảo](https://stanfordnlp.github.io/CoreNLP/download.html)<br/>
Tiến hành chạy chương trình
```sh
java -Xmx2g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000
```
Cài đặt thư viện stanfordnlp cho python
```sh
pip3 install stanfordnlp
```

Copy model đã được train sẵn theo dữ liệu của chúng tôi vào thư mục chứa StanfordCoreNLP. Thư mục chứa tại path/to/CS221.L11/standfordcorenlp/VnParser2.ser.gz
```sh
cp path/to/CS221.L11/standfordcorenlp/VnParser2.ser.gz VnParser2.ser.gz
```

Quay lại thư mục chứa đồ án
```sh
cd path/to/CS221.L11/standfordcorenlp/VnParser2.ser.gz
```

Chạy lệnh
```sh
python3 main.py -st
```
