init -1985:
    transform alpha_easein(duration):
        alpha 0.0
        easein duration alpha 1.0

    transform slide_up(leng=0, duration=0.0):
        yoffset leng
        easein duration yoffset 0

    transform yanchor_easein(duration):
        yanchor 1.0
        ypos 0.0

        on start:
            yanchor 0.0

        on show:
            easein duration yanchor 0.0

        on hide:
            easeout duration yanchor 1.0

    transform increase_xzoom:
        xzoom 0.0
        easein 0.2 xzoom 1.0
