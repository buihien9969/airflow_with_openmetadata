# OpenMetadata và Airflow Integration

Dự án này thiết lập môi trường để kết nối Apache Airflow với OpenMetadata, cho phép quản lý metadata và orchestration workflow.

## Tổng quan

Dự án sử dụng Docker Compose để triển khai các dịch vụ sau:
- **Apache Airflow**: Nền tảng workflow orchestration
- **OpenMetadata Integration**: Kết nối với OpenMetadata server để quản lý metadata

## Cấu trúc dự án

```
test_openmetadata/
├── dags/                      # Thư mục chứa DAG files cho Airflow
├── dag_generated_configs/     # Cấu hình DAG được tạo tự động bởi OpenMetadata
├── logs/                      # Log files
├── plugins/                   # Airflow plugins
├── .env                       # Biến môi trường
├── docker-compose.yml         # Cấu hình Docker Compose
└── README.md                  # Tài liệu dự án
```

## Yêu cầu

- Docker và Docker Compose
- Kết nối mạng đến OpenMetadata server (http://192.168.1.29:8585)

## Cài đặt và Khởi động

1. Clone repository:
   ```bash
   git clone <repository-url>
   cd test_openmetadata
   ```

2. Tạo file `.env` (nếu chưa có) với nội dung:
   ```
   AIRFLOW_UID=50000
   ```

3. Khởi động các dịch vụ:
   ```bash
   docker-compose up -d
   ```

4. Truy cập Airflow UI tại: http://localhost:8080
   - Username: airflow
   - Password: airflow

## Kết nối với OpenMetadata

Dự án đã được cấu hình để kết nối với OpenMetadata server tại:
- URL: http://192.168.1.29:8585/api
- Thông tin đăng nhập: Được cấu hình trong docker-compose.yml

## Quản lý DAG

- DAG files được lưu trong thư mục `dags/`
- OpenMetadata tự động tạo cấu hình DAG trong thư mục `dag_generated_configs/`

## Khắc phục sự cố

Nếu gặp vấn đề với quyền truy cập file:
1. Đảm bảo biến AIRFLOW_UID được đặt đúng trong file .env
2. Chạy lại lệnh `docker-compose up -d`

Nếu không thể kết nối với OpenMetadata:
1. Kiểm tra kết nối mạng đến server OpenMetadata
2. Xác minh thông tin đăng nhập trong docker-compose.yml

## Tài liệu tham khảo

- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
- [OpenMetadata Documentation](https://docs.open-metadata.org/)
