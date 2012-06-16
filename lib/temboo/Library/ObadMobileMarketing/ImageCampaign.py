
###############################################################################
#
# ImageCampaign
# Transfer an image for updating the email body image or the wap banner of a campaign.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ImageCampaign(Choreography):

    """
    Create a new instance of the ImageCampaign Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/ObadMobileMarketing/ImageCampaign')


    def new_input_set(self):
        return ImageCampaignInputSet()

    def _make_result_set(self, result, path):
        return ImageCampaignResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ImageCampaignChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ImageCampaign
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ImageCampaignInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((string) Private Key for 1 unique distributor - provided by Obad Mobile Marketing)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the CampaignID input for this choreography. ((integer) The ID of the campaign you want to update)
        """
        def set_CampaignID(self, value):
            InputSet._set_input(self, 'CampaignID', value)

        """
        Set the value of the ClientID input for this choreography. ((integer) Private Key for 1 unique customer to connect with - provided by Obad Mobile Marketing)
        """
        def set_ClientID(self, value):
            InputSet._set_input(self, 'ClientID', value)

        """
        Set the value of the Endpoint input for this choreography. ((string) The base URL for the server you want to access (i.e. http://10.10.10.1). Set this to the appropriate host for the demo sandbox or production.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the Type input for this choreography. ((optional, string) Specify the desired image type to modify (i.e. mailimage or wapban). Defaults to mailimage.)
        """
        def set_Type(self, value):
            InputSet._set_input(self, 'Type', value)

        """
        Set the value of the URLSource input for this choreography. ((string) The URL where you are hosting the JPG file (i.e. http://mybucket.s3.amazonaws.com/my_image.jpg))
        """
        def set_URLSource(self, value):
            InputSet._set_input(self, 'URLSource', value)


"""
A ResultSet with methods tailored to the values returned by the ImageCampaign choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ImageCampaignResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Obad)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ImageCampaignChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ImageCampaignResultSet(response, path)
