from lost.pyapi import script
import os
import random

class LostScript(script.Script):
    '''Set sim class for already present bounding boxes and request them again for annotation.
    Request images from first stage for review.
    
    Note:
        sim_classes from first annotation stage will be used.
    '''
    def main(self):
        for i, img in enumerate(self.inp.img_annos):
            if img.iteration == self.iteration:
                annos=[]
                anno_types=[]
                sim_class_list=[]
                anno_labels=[]
                for bbox in img.iter_annos('bbox'):
                    try:
                        sim_class_list.append(bbox.to_df()['anno_lbl_id'].values[0])
                    except:
                        sim_class_list.append(None)
                    annos.append(bbox.bbox)
                    anno_types.append('bbox')
                    anno_labels.append(bbox.labels[0].label_leaf_id)
                for point in img.iter_annos('point'):
                    try:
                        sim_class_list.append(point.to_df()['anno_lbl_id'].values[0])
                    except:
                        sim_class_list.append(None)
                    annos.append(point.point)
                    anno_types.append('point')
                    anno_labels.append(bbox.labels[0].label_leaf_id)
                for polygon in img.iter_annos('polygon'):
                    try:
                        sim_class_list.append(polygon.to_df()['anno_lbl_id'].values[0])
                    except:
                        sim_class_list.append(None)
                    annos.append(polygon.polygon)
                    anno_types.append('polygon')
                    anno_labels.append(bbox.labels[0].label_leaf_id)
                if len(annos)>0:
                    self.outp.request_annos(img, 
                        annos=annos, 
                        anno_types=anno_types,
                        anno_sim_classes=sim_class_list,
                        anno_labels=anno_labels) 
        self.logger.info(f"""Requested the following annos: \n{
            self.outp.to_vec(['anno_data', 'anno_sim_class', 'img_path'])
            }""")

if __name__ == "__main__":
    my_script = LostScript()
