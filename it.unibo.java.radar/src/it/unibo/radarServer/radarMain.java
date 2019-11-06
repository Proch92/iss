package it.unibo.radarServer;
import java.io.*;
import java.net.*;
import radarPojo.radarSupport;

public class radarMain {

	public static void main(String[] args) throws Exception {
		radarSupport radar = new radarSupport();
		radar.setUpRadarGui();
		
		ServerSocket server = new ServerSocket(6789);
		Socket socket = server.accept();
		
		String distance;
		int dist;
		
		while (true) {
			BufferedReader buffIn = new BufferedReader(new InputStreamReader(socket.getInputStream()));
			distance = buffIn.readLine();
			dist = 0;
			
			try {
				dist = Integer.parseInt(distance);
			} catch(Exception e) {}
			
			System.out.println(dist);
			radar.update(Integer.toString(dist), "0");
		}
	}

}
