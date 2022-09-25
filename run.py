from app import recognition_liveness

if __name__ == '__main__':
    name, label_name = recognition_liveness('liveness.model', 'label_encoder.pickle',
                                            'face_detector',  confidence=0.7)
    print(name, label_name)