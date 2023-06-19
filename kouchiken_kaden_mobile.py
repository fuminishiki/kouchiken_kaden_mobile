import folium

m = folium.Map(location=[33.2358698,133.4131488],zoom_start=9)
m

folium.Marker(location=[33.5025368,133.9006689],popup='ヤマダデンキ テックランド高知安芸店　　　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[33.5563538,133.5105291],popup='ヤマダデンキ テックランド高知旭店　　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[33.5008017,133.2974498],popup='ヤマダデンキ テックランド高知佐川店　　　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[32.979881,132.9136878],popup='ヤマダデンキ テックランド高知四万十店　　　　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[33.4097296,133.2914198],popup='ヤマダデンキ テックランド高知須崎店　　　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[33.5788804,133.5524171],popup='ヤマダデンキ テックランド高知店　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[33.4966585,133.4355591],popup='ヤマダデンキ テックランド高知土佐店　　　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[32.9281193,132.7035299],popup='ヤマダデンキ テックランド宿毛店　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[33.5616904,133.5988045],popup='ヤマダデンキ Tecc LIFE SELECT 高知本店　　　　　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[33.5665444,133.5458078],popup='ケーズデンキ 高知駅前店　　　　　　　　　　　',icon=folium.Icon(color="orange")).add_to(m)
m

folium.Marker(location=[33.4100818,133.2986797],popup='ケーズデンキ 須崎店　　　　　　　　　',icon=folium.Icon(color="orange")).add_to(m)
m

folium.Marker(location=[33.5772513,133.5421815],popup='イオンモバイル 高知店　　　　　　　　　　',icon=folium.Icon(color="purple")).add_to(m)
m

folium.Marker(location=[33.5416020,133.4969984],popup='PC DEPOT 土佐道路店　　　　　　　　　　',icon=folium.Icon(color="beige")).add_to(m)
m

folium.Marker(location=[33.8369974,132.7651728],popup='マーキュリー 松山　　　　　　　　',icon=folium.Icon(color="white")).add_to(m)
m

m.save('kouchiken_kaden_mobile.html')
