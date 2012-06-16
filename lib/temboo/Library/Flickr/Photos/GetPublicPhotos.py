
###############################################################################
#
# GetPublicPhotos
# Obtain a list of public photos for a given user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetPublicPhotos(Choreography):

    """
    Create a new instance of the GetPublicPhotos Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Flickr/Photos/GetPublicPhotos')


    def new_input_set(self):
        return GetPublicPhotosInputSet()

    def _make_result_set(self, result, path):
        return GetPublicPhotosResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetPublicPhotosChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetPublicPhotos
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetPublicPhotosInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) Enter your application API key.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Extras input for this choreography. ((optional, string) A comma-separated list returning additional photo information such as: license, description, date_upload, date_taken.  Additional options are listed on this method's API doc page.)
        """
        def set_Extras(self, value):
            InputSet._set_input(self, 'Extras', value)

        """
        Set the value of the Page input for this choreography. ((optional, integer) Specify the page of photos that is to be returned.  If unspecified, the first page is returned.)
        """
        def set_Page(self, value):
            InputSet._set_input(self, 'Page', value)

        """
        Set the value of the PerPage input for this choreography. ((optional, integer) Specify how many photos to display per page. Default is set to: 100. The mamimum allowed value is: 500.)
        """
        def set_PerPage(self, value):
            InputSet._set_input(self, 'PerPage', value)

        """
        Set the value of the SafeSearch input for this choreography. ((optional, integer) Specify a safe search setting by entering: 1 (for safe), 2 (moderate), 3 (restricted).  Default is set to: 1 (safe).)
        """
        def set_SafeSearch(self, value):
            InputSet._set_input(self, 'SafeSearch', value)

        """
        Set the value of the UserID input for this choreography. ((required, string) Enter the NSID of the user whose public photos are being retrieved.)
        """
        def set_UserID(self, value):
            InputSet._set_input(self, 'UserID', value)


"""
A ResultSet with methods tailored to the values returned by the GetPublicPhotos choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetPublicPhotosResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response in XML from Flickr.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetPublicPhotosChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetPublicPhotosResultSet(response, path)
