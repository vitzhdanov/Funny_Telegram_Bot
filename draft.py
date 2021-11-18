
t = [{'495432329': '495432329: 495432329', 'name': 'Vladislav', 'value': 4}, {'495432329': '495432: 495432329', 'name': 'dwefwe', 'value': 4}, {'712795671': '712795671: 1695879234', 'name': 'Ренат', 'value': 4}]
u = '495432329: 495432329'
y = [{'chat_id': '495432329', 'value': 4}, {'chat_id': '495432329', 'value': 4}]
# for i in t:
#     for k, v in i.items():
#         if k == '495432329':
#             y.append(
#                 {
#                     'chat_id': '495432329',
#                     'value': i['value']
#                 }
#             )
print([i for i in y if i['chat_id']=='495432329'])
