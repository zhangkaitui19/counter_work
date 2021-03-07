from dearpygui.core import *
from dearpygui.simple import *

t1 = 0
t2 = 0
qc = 0



class ConstructGui:

	def __init__(self, width, height):
		self.width = width
		self.height = height


	def builder(self):
		set_main_window_title('Ticket Counter')
		set_main_window_size(self.width,self.height)
		set_theme('Dark 2')
		LoginScreen()

	@staticmethod
	def run_app():
		start_dearpygui(primary_window='Jake counter')

class LoginScreen:

	def __init__(self):
		set_render_callback(self.auto_center)
		#this is to remove style borders, padding and spacings from the main window which mess up spacing calculation
		set_item_style_var('Jake counter', mvGuiStyleVar_WindowPadding, [0,0])
		set_item_style_var('Jake counter', mvGuiStyleVar_ItemSpacing, [0,0])
		set_item_style_var('Jake counter', mvGuiStyleVar_ItemInnerSpacing, [0,0])
		set_item_style_var('Jake counter', mvGuiStyleVar_WindowBorderSize, [0])
		self.t2_counter = 0


	def auto_center(self, sender, data):
		#getting the window sizes
		main_width = get_item_width('Jake counter')
		main_height = get_item_height('Jake counter')


	def theme_setting(sender, data):
		set_theme(data)	

	def t2_tick():
		
		# self.t2_counter += 1

		delete_item('##list2')
		add_listbox('##list2', before='\n\n ') #items=str(t2_counter))
	


	 #items=str(t2_counter)
	


	with window('Jake counter'):

		with child(name='chi', border=False, autosize_x=True, autosize_y=True):
			add_separator()

			with menu_bar(name='menu'):

				
				with menu(name='themes'):

					
					add_menu_item(parent='themes', name='Classic', callback=theme_setting, callback_data='Classic')
					add_menu_item(parent='themes', name='Light', callback=theme_setting, callback_data='Light')
					add_menu_item(parent='themes', name='Dark', callback=theme_setting, callback_data='Dark')
					add_menu_item(parent='themes', name='Dark 2', callback=theme_setting, callback_data='Dark 2')
					add_menu_item(parent='themes', name='Cherry', callback=theme_setting, callback_data='Red')
					end()

				add_text('\n\n')
				add_text(f'T1 tickets: {str(t1)}')

				def t1_tick():
					global t1
					delete_item(f'T1 tickets: {str(t1)}')
					t1 += 1
					add_text(f'T1 tickets: {str(t1)}', before=' \n\n')

				def t1_downtick():
					global t1
					delete_item(f'T1 tickets: {str(t1)}')
					t1 -= 1
					add_text(f'T1 tickets: {str(t1)}', before=' \n\n')
				
				add_text(' \n\n')
				add_button(name='Add T1', width=60, height=40, callback=t1_tick)
				add_same_line(spacing=10)
				add_button(name='Reduce T1', height=40, callback=t1_downtick)
				add_separator()

				add_text('  \n\n')
				add_text(f'T2 tickets: {str(t2)}')

				def t2_tick():
					global t2
					delete_item(f'T2 tickets: {str(t2)}')
					t2 += 1
					add_text(f'T2 tickets: {str(t2)}', before='   \n\n')

				def t2_downtick():
					global t2
					delete_item(f'T2 tickets: {str(t2)}')
					t2 -= 1
					add_text(f'T2 tickets: {str(t2)}', before='   \n\n')
					
				add_text('   \n\n')
				add_button(name='Add T2', width=60, height=40, callback=t2_tick)
				add_same_line(spacing=10)
				add_button(name='Reduce T2', height=40, callback=t2_downtick)
				add_separator()


				add_text('    \n\n')
				qc_text = add_text(f'QC tickets: {str(qc)}')

				def qc_tick():
					global qc
					delete_item(f'QC tickets: {str(qc)}')
					qc += 1
					add_text(f'QC tickets: {str(qc)}', before='     \n\n')

				def qc_downtick():
					global qc
					delete_item(f'QC tickets: {str(qc)}')
					qc -= 1
					add_text(f'QC tickets: {str(qc)}', before='     \n\n')

					
				add_text('     \n\n')
				add_button(name='Add QC', width=60, height=40, callback=qc_tick)
				add_same_line(spacing=10)
				add_button(name='Reduce QC', height=40, callback=qc_downtick)
				add_separator()
				# add_same_line(spacing=10)

				


# show_style_editor()

if __name__ == '__main__':
	base = ConstructGui(500, 650)
	base.builder()
	base.run_app()