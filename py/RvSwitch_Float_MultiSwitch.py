from ..core import CATEGORY

class RvSwitch_Float_MultiSwitch:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
            },
            "optional": {
                "input1": ("FLOAT", {"forceInput": True}),
                "input2": ("FLOAT", {"forceInput": True}),
                "input3": ("FLOAT", {"forceInput": True}),
                "input4": ("FLOAT", {"forceInput": True}),
                "input5": ("FLOAT", {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.MULTISWITCHES.value
    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("float",)

    FUNCTION = "execute"

    def execute(self, input1=None, input2=None, input3=None, input4=None, input5=None):
        
        if input1 != None:
            return (input1,)
        elif input2 != None:
            return (input2,)
        elif input3 != None:
            return (input3,)
        elif input4 != None:
            return (input4,)
        elif input5 != None:
            return (input5,)
        else:
            raise ValueError("Missing Input: Multi Float Switch has no active Input")

NODE_NAME = 'Float Multi-Switch // RvTools'
NODE_DESC = 'Float Multi-Switch'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSwitch_Float_MultiSwitch
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
