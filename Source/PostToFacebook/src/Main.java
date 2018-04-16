import com.restfb.*;
import com.restfb.batch.BatchRequest;
import com.restfb.batch.BatchResponse;
import com.restfb.exception.devicetoken.FacebookDeviceTokenCodeExpiredException;
import com.restfb.exception.devicetoken.FacebookDeviceTokenDeclinedException;
import com.restfb.exception.devicetoken.FacebookDeviceTokenPendingException;
import com.restfb.exception.devicetoken.FacebookDeviceTokenSlowdownException;
import com.restfb.scope.ScopeBuilder;
import com.restfb.types.DeviceCode;
import com.restfb.types.FacebookType;
import com.restfb.types.User;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Date;
import java.util.List;

public class Main {

    public static void main(String args[]) throws FileNotFoundException {
        String userAccessToken = "EAACEdEose0cBANvHRRZCwPt4oWuvEZBGFCd60aTZBZCDZB14ZBNSTQ5ZAH77hSkoAJJBtIpiRp1jRfAz6lPAry9Jt1L0VIQAUZADVbhUZCJUZAot5ItMrH8qheV2eHssaSDFjcoyzFdA27zLA4HIE9vYqMLBxRfvFA4R1QHUX6BIc2n6NVC2BfH2c7Dqyiamxl2ZBP1JMIfWyMmaQZDZD";
        FacebookClient fbClient = new DefaultFacebookClient(userAccessToken);

        FileInputStream fis = new FileInputStream(new File("C:\\Users\\MuthaNagaVenkataSaty\\Desktop\\myself.jpg"));
        //FileInputStream fis = new FileInputStream(new File("C:\\Users\\MuthaNagaVenkataSaty\\Desktop\\k.mkv"));
        //FacebookType response = fbClient.publish("me/videos", FacebookType.class,BinaryAttachment.with("k.mkv",fis),Parameter.with("message","Publishing video to FB")); //POST Request
        //FacebookType response = fbClient.publish("me/photos", FacebookType.class,BinaryAttachment.with("myself.jpg",fis)); //POST Request
        FacebookType response = fbClient.publish("me/feed", FacebookType.class,Parameter.with("message","Posting to my FB timeline")); //POST Request

        System.out.println(response.getId());
        User me = fbClient.fetchObject("me",User.class);
        System.out.println(me.getName());


    }
}
