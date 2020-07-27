import copy

def manhattan_distance(wires_coordinates):
    # wire_1 = ["R8", "U5", "L5", "D3"]
    # wire_2 = ["U7", "R6", "D4", "L4"]


    # segment_x = 0
    # segment_y = 0
    # position = dict.fromkeys(['x', 'y'], 0)
    
    # start_segment = dict.fromkeys(['x', 'y'], 0)
    general_array = [[], []]

    segment_map = {'from': {'x': 0, 'y': 0}, 'to': {'x': 0, 'y': 0}}
    temp_dict = []

    counter = 0
    for string_mass in wires_coordinates:
        
        segment_x = 0
        segment_y = 0
        position = dict.fromkeys(['x', 'y'], 0)
        
        start_segment = dict.fromkeys(['x', 'y'], 0)

        for elem in string_mass:
            elem_index = int(elem.replace(elem[0], ''))

            if elem[0] == "U":
                segment_y += elem_index

            if elem[0] == "R":
                segment_x += elem_index

            if elem[0] == "D":
                segment_y -= elem_index

            if elem[0] == "L":
                segment_x -= elem_index


            position.update({
                'x': segment_x,
                'y': segment_y,
            })

            #############
            # if position.get('x') < start_segment.get('x') or position.get('y') < start_segment.get('y'):
            #     segment_map.update({
            #         'from': position,
            #         'to': start_segment,
            #     })
            # else:
            #     segment_map.update({
            #         'from': start_segment,
            #         'to': position,
            #     })
            
            ##############

            segment_map.update({
                'from': start_segment,
                'to': position,
            })

            temp_dict.append(segment_map['from'].copy())
            temp_dict.append(segment_map['to'].copy())

            if segment_map['from'].get('x') == segment_map['to'].get('x'):
                temp_dict.append(abs(segment_map['from'].get('y') - segment_map['to'].get('y')))
            else:
                temp_dict.append(abs(segment_map['from'].get('x') - segment_map['to'].get('x')))


            general_array[counter].append(temp_dict.copy())

            temp_dict.clear()
            # general_array[counter].append(segment_map['from'].copy())
            # general_array[counter].append(segment_map['to'].copy())
            

            start_segment.update({
                'x': position['x'],
                'y': position['y'],
            })

        counter += 1

    distance = []
    intersections = []
    curent_lengt = 0
    curent_lengt2 = 0
    vector_length = []
    
    

    for i in range(0, len(general_array[0])):
        

        curent_lengt2 += general_array[0][i][2]
        print("first", general_array[0][i][2])
        curent_lengt = 0
        
        for j in range(0, len(general_array[1])):

            
            # print(general_array[1][j][0].get('x'), general_array[1][j][1].get('x'))
            curent_lengt += general_array[1][j][2]
            

            if general_array[0][i][0].get('x') == general_array[0][i][1].get('x'): #or general_array[0][i][0].get('y') == general_array[0][i][1].get('y'):
                vertical = general_array[0][i]
                horizontal = general_array[1][j]


            if general_array[1][j][0].get('x') == general_array[1][j][1].get('x'):  #or general_array[1][j][0].get('y') == general_array[1][j][1].get('y'):
                vertical = general_array[1][j]
                horizontal = general_array[0][i]
            
            if general_array[0][i][0].get('y') == general_array[0][i][1].get('y') and general_array[1][j][0].get('y') == general_array[1][j][1].get('y'):
                continue

            minX = min(horizontal[0].get('x'), horizontal[1].get('x'))
            maxX = max(horizontal[0].get('x'), horizontal[1].get('x'))

            minY = min(vertical[0].get('y'), vertical[1].get('y'))
            maxY = max(vertical[0].get('y'), vertical[1].get('y'))

            
            if (minX <= vertical[0].get('x') and vertical[0].get('x') <= maxX) and (minY <= horizontal[0].get('y') and horizontal[0].get('y') <= maxY):
                if abs(vertical[0].get('x')) + abs(horizontal[0].get('y')) != 0:
                    distance.append(abs(vertical[0].get('x')) + abs(horizontal[0].get('y')))
                    
                    print(curent_lengt, curent_lengt2, vertical, horizontal)
                    print(vertical[0].get('x'), horizontal[0].get('y'))

                    # print("second", general_array[1][j][2])
                    temp = abs(horizontal[0].get('y') - minX)
                    temp1 = abs(vertical[0].get('x') - minY)
                    print("temp: ", temp, "temp1: ", temp1)
                    vector_length.append((curent_lengt - abs(temp)) + (curent_lengt2 - abs(temp1)))

                    
                    print(vector_length)
                    


    if len(distance):
        print("The manhattan distance is: ", min(distance))
        
        print(distance)
            # (min(x1, x2) <= x3 and x3 <= max(x1, x2)) and (min(y1, y2) <= y3 and y3 <= max(x1, x2)) # => BETWEEN


            # (x1 <= max(y3, y4) and x1 >= max(y3, y4)) and (y1 <= max(x3, x4) and y1 >= min(x3, x4))




#    (3-3)x+(2-6)y+(6*3-2*3)=0
#    (5-2)x+(3-3)y+(3*2-3*5)=0


if __name__ == "__main__":
    
    wires_coordinates = []
    
    with open("puzzle_input", "r") as file:
        for i in file:
            wires_coordinates.append(i.split(','))
    # wires_coordinates = wires_coordinates[0] + wires_coordinates[1]
        
    manhattan_distance(wires_coordinates)