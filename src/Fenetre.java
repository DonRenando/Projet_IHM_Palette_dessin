import fr.dgac.ivy.IvyException;

import javax.swing.*;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.event.MouseMotionListener;

/**
 * Created by renando on 16/01/17.
 */
class Fenetre extends JFrame {
    private ivyTranslater monIvy;

    //private Automate a;


    Fenetre(Panel panel) {
        super("IHM TP Lines");
        this.setDefaultCloseOperation(EXIT_ON_CLOSE);
        Panel panel1 = panel;
        this.add(panel);
        try {
            this.monIvy = new ivyTranslater();
        } catch (IvyException e) {
            e.printStackTrace();
        }
        panel.addMouseListener(new MouseListener() {
            @Override
            public void mouseClicked(MouseEvent mouseEvent) {
            }


            @Override
            public void mousePressed(MouseEvent mouseEvent) {
                if (SwingUtilities.isLeftMouseButton(mouseEvent))
                    panel.getStroke().addPoint(mouseEvent.getX(), mouseEvent.getY());
                panel.stroke = new Stroke();
            }

            @Override
            public void mouseReleased(MouseEvent mouseEvent) {
                monIvy.sendMsg("coord=" + panel.getStroke().toString());
            }


            @Override
            public void mouseEntered(MouseEvent mouseEvent) {
            }

            @Override
            public void mouseExited(MouseEvent mouseEvent) {
            }
        });

        panel.addMouseMotionListener(new MouseMotionListener() {

            @Override
            public void mouseDragged(MouseEvent mouseEvent) {
                if (SwingUtilities.isLeftMouseButton(mouseEvent))
                    panel.getStroke().addPoint(mouseEvent.getX(), mouseEvent.getY());
                panel.repaint();

            }

            @Override
            public void mouseMoved(MouseEvent mouseEvent) {
            }

        });


        setSize(600, 600);
        setVisible(true);


    }


}
