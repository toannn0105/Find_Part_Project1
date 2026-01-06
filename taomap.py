import osmnx as ox

# Sử dụng tọa độ trung tâm Hà Nội (Khu vực gần hồ Hoàn Kiếm/Ba Đình)
center_point = (21.0285, 105.8542) 

# Lấy dữ liệu trong bán kính 10km (Bao phủ hầu hết các quận nội thành: Ba Đình, Hoàn Kiếm, Tây Hồ, Cầu Giấy, Đống Đa...)
# network_type="drive" sẽ giúp file nhẹ hơn và tìm đường chính xác hơn cho ô tô/xe máy
G = ox.graph_from_point(center_point, dist=10000, network_type="drive", simplify=True)

# Lưu lại file với tên bạn đã khai báo trong Deploy.py
ox.save_graphml(G, "noithanh_hanoi_graph.graphml")

print("Đã tạo bản đồ nội thành Hà Nội thành công!")
