# from ursina import *

# def create_rounded_button(text='', width=0.4, height=0.1, radius=0.25, position=(0,0)):
#     # Вычисляем радиус относительно меньшей стороны, чтобы он всегда был аккуратным
#     # Либо используем фиксированное значение.
    
#     button = Button(
#         text=text,
#         position=position,
#         scale=(width, height),
#         # Ключевой момент: создаем Quad с учетом соотношения сторон (aspect)
#         model=Quad(radius=radius, aspect=width/height),
#         color=color.azure
#     )
#     return button

# # 1. Обычная кнопка (углы растянуты в овалы)
# bad_button = Button(
#     text='Stretched Corners',
#     scale=(0.6, 0.15),
#     position=(0, 0.2),
#     radius=0.5,
#     color=color.red
# )

# # 2. Кнопка через нашу функцию (идеально круглые углы)
# good_button = create_rounded_button(
#     text='Perfect Corners',
#     width=0.6,
#     height=0.15,
#     radius=0.2,
#     position=(0, -0.2)
# )

# app = Ursina()

# EditorCamera()
# app.run()


#*************************************


# from ursina import *

# app = Ursina()

# def create_custom_button(text='', w=0.5, h=0.2, r=0.2, pos=(0,0)):
#     # Создаем сущность
#     btn = Entity(
#         parent=camera.ui,
#         model=Quad(radius=r, aspect=w/h), # Геометрия с учетом пропорций
#         texture='white_cube',             # Базовая текстура для цвета
#         color=color.hex('#1240AB'),
#         scale=(w, h),
#         position=pos,
#         collider='box'                    # Добавляем коллайдер для кликов
#     )
    
#     # Добавляем текст поверх
#     btn_text = Text(text=text, parent=btn, origin=(0,0), scale=(1/w * 2, 1/h * 2))
    
#     # Логика взаимодействия (аналог Button)
#     def on_mouse_enter():
#         btn.color = color.hex('#4671D5')
        
#     def on_mouse_exit():
#         btn.color = color.hex('#1240AB')

#     def on_click():
#         print(f"Кнопка '{text}' нажата!")
#         # btn.color=color.hex('#06266F')
#         btn.shake()
#         # btn.color = color.hex('#4671D5')

#     # Привязываем функции к событиям мыши
#     btn.on_mouse_enter = on_mouse_enter
#     btn.on_mouse_exit = on_mouse_exit
#     btn.on_click = on_click
    
#     return btn

# # Примеры
# b1 = create_custom_button("Entity Button", w=0.6, h=0.2, r=0.3, pos=(0, 0.1))
# b2 = create_custom_button("Slim Button", w=0.8, h=0.1, r=0.5, pos=(0, -0.2))

# app.run()



#*************************************


# from ursina import *

# app = Ursina()

# def create_animated_button(text='', w=0.5, h=0.2, r=0.2, pos=(0,0)):
#     # Базовые параметры
#     base_color = color.azure
#     hover_color = color.cyan
#     base_scale = Vec2(w, h)
#     hover_scale = base_scale * 1.05 # Увеличиваем на 5% при наведении
    
#     btn = Entity(
#         parent=camera.ui,
#         model=Quad(radius=r, aspect=w/h),
#         color=base_color,
#         scale=base_scale,
#         position=pos,
#         collider='box'
#     )
    
#     Text(text=text, parent=btn, origin=(0,0), scale=(1/w * 2, 1/h * 2))
    
#     # Анимация при наведении
#     btn.on_mouse_enter = lambda: [
#         btn.animate_color(hover_color, duration=0.1),
#         btn.animate_scale(hover_scale, duration=0.1, curve=curve.out_expo)
#     ]
    
#     # Возврат в исходное состояние
#     btn.on_mouse_exit = lambda: [
#         btn.animate_color(base_color, duration=0.1),
#         btn.animate_scale(base_scale, duration=0.1, curve=curve.out_expo)
#     ]

#     return btn

# # Создаем кнопку
# button = create_animated_button("Hover Me", w=0.5, h=0.15, r=0.4)

# app.run()



#*************************************


# from ursina import *

# app = Ursina()

# def create_pulsing_button(text='', w=0.5, h=0.2, r=0.2, pos=(0,0)):
#     base_scale = Vec2(w, h)
#     hover_scale = base_scale * 1 #1.05
#     click_scale = base_scale * 0.9 # Размер при нажатии (чуть меньше оригинала)
    
#     btn = Entity(
#         parent=camera.ui,
#         model=Quad(radius=r, aspect=w/h),
#         color=color.azure,
#         scale=base_scale,
#         position=pos,
#         collider='box'
#     )
    
#     Text(text=text, parent=btn, origin=(0,0), scale=(1/w * 2, 1/h * 2))
    
#     # Логика наведения
#     btn.on_mouse_enter = lambda: btn.animate_scale(hover_scale, duration=0.1)
#     btn.on_mouse_exit = lambda: btn.animate_scale(base_scale, duration=0.1)

#     # Эффект пульсации при клике
#     def on_click():
#         # Сжимаем и тут же возвращаем в hover_scale
#         btn.animate_scale(click_scale, duration=0.05, curve=curve.linear)
#         invoke(btn.animate_scale, hover_scale, duration=0.1, delay=0.05)
        
#         print("Click!")

#     btn.on_click = on_click
#     return btn

# create_pulsing_button("Pulse Button", w=0.4, h=0.15, r=0.5)

# app.run()

