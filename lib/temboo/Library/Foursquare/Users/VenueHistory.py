
###############################################################################
#
# VenueHistory
# Returns a list of all venues visited by the specified user, along with how many visits and when they were last there. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class VenueHistory(Choreography):

    """
    Create a new instance of the VenueHistory Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Users/VenueHistory')


    def new_input_set(self):
        return VenueHistoryInputSet()

    def _make_result_set(self, result, path):
        return VenueHistoryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return VenueHistoryChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the VenueHistory
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class VenueHistoryInputSet(InputSet):
        """
        Set the value of the AfterTimeStamp input for this choreography. ((optional, date) Retrieve the first results after the seconds entered since epoch time.)
        """
        def set_AfterTimeStamp(self, value):
            InputSet._set_input(self, 'AfterTimeStamp', value)

        """
        Set the value of the BeforeTimeStamp input for this choreography. ((optional, date) Retrieve the first results prior to the seconds specified. Useful for paging backward in time.)
        """
        def set_BeforeTimeStamp(self, value):
            InputSet._set_input(self, 'BeforeTimeStamp', value)

        """
        Set the value of the CategoryID input for this choreography. ((optional, string) Limits returned venues to those in this category. If specifying a top-level category, all sub-categories will also match the query.)
        """
        def set_CategoryID(self, value):
            InputSet._set_input(self, 'CategoryID', value)

        """
        Set the value of the OauthToken input for this choreography. ((required, string) The Foursquare API Oauth token string.)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the UserID input for this choreography. ((optional, string) Only 'self' is supported at this moment by the Foursquare API. Defaults to: self.)
        """
        def set_UserID(self, value):
            InputSet._set_input(self, 'UserID', value)


"""
A ResultSet with methods tailored to the values returned by the VenueHistory choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class VenueHistoryResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class VenueHistoryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return VenueHistoryResultSet(response, path)
