import fr.dgac.ivy.IvyException;
import model.Forme;

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
                if (!panel.getStroke().isEmpty())
                    monIvy.sendMsg("coord=" + panel.getStroke().toString());

                panel.getStroke().normalize();
                System.out.println(panel.getStroke());
                Reconnaissance.comparaison(Reconnaissance.reconnaissance(panel.getStroke(), Forme.ROND.split(";")),
                        Reconnaissance.reconnaissance(panel.getStroke(), Forme.CARRE.split(";")),
                        Reconnaissance.reconnaissance(panel.getStroke(), Forme.TRAIT.split(";")),
                        Reconnaissance.reconnaissance(panel.getStroke(), Forme.Z.split(";")));

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
