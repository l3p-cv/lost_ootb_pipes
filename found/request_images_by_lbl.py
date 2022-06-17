from lost.pyapi import script
import os

ENVS = ['lost']
ARGUMENTS = {'lbls' : { 'value': ["annotate"],
                            'help': 'List of labels that that should be annotated'}
            }
class LostScript(script.Script):
    '''Request annos for images with a label again.
    '''
        
    def img_lbls_in_allowed_lbls(self, allowed, img_lbls):
        for lbl in img_lbls:
            if lbl in allowed:
                return True

    def main(self):
        allowed_lbls = self.get_arg('lbls')
        if not isinstance(allowed_lbls, list):
            allowed_lbls = [allowed_lbls]
        for i, img in enumerate(self.inp.img_annos): 
            img_lbls = img.to_vec('img_lbl')[0]
            if self.img_lbls_in_allowed_lbls(allowed_lbls, img_lbls):
                self.outp.request_annos(img)

if __name__ == "__main__":
    my_script = LostScript() 
