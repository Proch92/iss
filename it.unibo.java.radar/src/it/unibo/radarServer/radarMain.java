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
		BufferedReader buffIn = new BufferedReader(new InputStreamReader(socket.getInputStream()));
		DataOutputStream buffOut = new DataOutputStream(socket.getOutputStream());
		
		while (true) {
			int distance = tryCastInt(receive(buffIn));
			
			System.out.println(distance);
			radar.update(Integer.toString(distance), "0");
			
			ack(buffOut);
		}
	}
	
	private static String receive(BufferedReader buffIn) throws Exception {
		return buffIn.readLine();
	}
	
	private static int tryCastInt(String message) {
		int dist = 0;
		try {
			dist = Integer.parseInt(message);
		} catch(Exception e) {}
		return dist;
	}
	
	private static void ack(DataOutputStream buffOut) throws Exception {
		buffOut.writeBytes("ACK\n");
	}

}
