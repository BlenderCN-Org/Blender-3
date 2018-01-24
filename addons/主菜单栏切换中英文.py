bl_info = {
    "name": "主菜单栏切换中英文",      #插件名字
    "author": "黑猫鸣泣时",          #作者名字
    "version": (1, 1),               #插件版本
    "blender": (2, 78, 0),           #blender版本
    "location": "3DView > Header",   #插件所在位置
    "description": "在主菜单栏切换中英文",       #描述
    "warning": "警告!",              #警告
    "wiki_url": "http://tieba.baidu.com/"
                "p/4969706030",      #文档地址
    "support": 'OFFICIAL',           #支持??
    "category": "Development",       #分类
}
import bpy
 
class panel_2(bpy.types.Header):  
    bl_space_type = 'INFO'  
    def draw(self, context):
        layout = self.layout
        layout.prop(bpy.context.user_preferences.system, "use_translate_interface", text="中英文切换", toggle=True)
         
         
def register():                           
    bpy.utils.register_module(__name__)    
     
def unregister():                          
    bpy.utils.unregister_module(__name__)  
 
if __name__ == "__main__":
    register()
