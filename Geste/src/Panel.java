import javax.swing.*;
import java.awt.*;
import java.awt.geom.Point2D;

/**
 * Created by renando on 16/01/17.
 */
public class Panel extends JComponent {


    public Stroke stroke;

    public Panel() {
        super();
        stroke = new Stroke();
    }

    @Override
    protected void paintComponent(Graphics graphics) {
        super.paintComponent(graphics);
        Graphics2D g2 = (Graphics2D) graphics;

        for (Point2D.Double p : stroke.getPoints()) {
            int x = (int) p.getX();
            int y = (int) p.getY();
            g2.drawOval(x, y, 2, 2);

        }

    }

    public Stroke getStroke() {
        return stroke;
    }

    public void setStroke(Stroke stroke) {
        this.stroke = stroke;
    }

}
