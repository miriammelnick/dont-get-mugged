
###############################################################################
#
# GetBase64EncodedPhoto
# Retrieves a photo from a constructed source URL and returns the file content as Base64 encoded data.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetBase64EncodedPhoto(Choreography):

    """
    Create a new instance of the GetBase64EncodedPhoto Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Flickr/Photos/GetBase64EncodedPhoto')


    def new_input_set(self):
        return GetBase64EncodedPhotoInputSet()

    def _make_result_set(self, result, path):
        return GetBase64EncodedPhotoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetBase64EncodedPhotoChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetBase64EncodedPhoto
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetBase64EncodedPhotoInputSet(InputSet):
        """
        Set the value of the FarmID input for this choreography. ((required, integer) The farm id associated with the photo. This is returned by many API methods associated with photo details.)
        """
        def set_FarmID(self, value):
            InputSet._set_input(self, 'FarmID', value)

        """
        Set the value of the ImageType input for this choreography. ((optional, string) The image type. Valid values are: jpg, png, or gif. Defaults to "jpg".)
        """
        def set_ImageType(self, value):
            InputSet._set_input(self, 'ImageType', value)

        """
        Set the value of the PhotoID input for this choreography. ((required, integer) The id of the photo you to download.)
        """
        def set_PhotoID(self, value):
            InputSet._set_input(self, 'PhotoID', value)

        """
        Set the value of the Secret input for this choreography. ((required, string) The secret associated with the photo. This is returned by many API methods associated with photo details.)
        """
        def set_Secret(self, value):
            InputSet._set_input(self, 'Secret', value)

        """
        Set the value of the ServerID input for this choreography. ((required, integer) The server id associated with the photo. This is returned by many API methods associated with photo details.)
        """
        def set_ServerID(self, value):
            InputSet._set_input(self, 'ServerID', value)


"""
A ResultSet with methods tailored to the values returned by the GetBase64EncodedPhoto choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetBase64EncodedPhotoResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((string) The Base64 encoded image content.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetBase64EncodedPhotoChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetBase64EncodedPhotoResultSet(response, path)
