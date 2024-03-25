class Settings:
    screenSize: tuple[int]   = ()
    surfaceSize: tuple[int]  = ()
    rotateKoeficient: float = 2
    rotateAngle: int        = 0
    active: bool            = False
    editor: bool            = False
    background: bool        = True

    def __init__(self, screenSize: tuple) -> None:
        self.screenSize = screenSize
        self.surfaceSize = (max(screenSize)+120, max(screenSize)+120)

    def get_screen_size(self) -> tuple[int]:
        return self.screenSize
    
    def get_surface_size(self) -> tuple[int]:
        return self.surfaceSize
    
    def change_the_rotate_angle(self, koeficient: int) -> None:
        self.rotateAngle -= koeficient

    def reset_rotate_angle(self) -> None:
        self.rotateAngle = 0

    def get_active_state(self) -> bool:
        if self.active:
            return True
        return False
        
    def get_editor_state(self) -> bool:
        if self.editor:
            return True
        return False
    
    def get_background_state(self) -> bool:
        if self.background:
            return True
        return False
        
    def editor_on(self) -> None:
        self.editor = True

    def editor_off(self) -> None:
        self.editor = False

    def background_on(self) -> None:
        self.background = True

    def background_off(self) -> None:
        self.background = False

    def stop(self) -> None:
        self.active = False
        
    def play(self) -> None:
        self.active = True



